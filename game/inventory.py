"""Inventory management APIs."""
from collections import defaultdict
from typing import Dict, Iterable, Iterator, Set, Tuple

from dcs.unittype import UnitType

from gen.flights.flight import Flight
from theater import ControlPoint


class ControlPointAircraftInventory:
    """Aircraft inventory for a single control point."""

    def __init__(self, control_point: ControlPoint) -> None:
        self.control_point = control_point
        self.inventory: Dict[UnitType, int] = defaultdict(int)

    def add_aircraft(self, aircraft: UnitType, count: int) -> None:
        """Adds aircraft to the inventory.

        Args:
            aircraft: The type of aircraft to add.
            count: The number of aircraft to add.
        """
        self.inventory[aircraft] += count

    def remove_aircraft(self, aircraft: UnitType, count: int) -> None:
        """Removes aircraft from the inventory.

        Args:
            aircraft: The type of aircraft to remove.
            count: The number of aircraft to remove.

        Raises:
            ValueError: The control point cannot fulfill the requested number of
            aircraft.
        """
        available = self.inventory[aircraft]
        if available < count:
            raise ValueError(
                f"Cannot remove {count} {aircraft.id} from "
                f"{self.control_point.name}. Only have {available}."
            )
        self.inventory[aircraft] -= count

    def available(self, aircraft: UnitType) -> int:
        """Returns the number of available aircraft of the given type.

        Args:
            aircraft: The type of aircraft to query.
        """
        return self.inventory[aircraft]

    @property
    def types_available(self) -> Iterator[UnitType]:
        """Iterates over all available aircraft types."""
        for aircraft, count in self.inventory.items():
            if count > 0:
                yield aircraft

    @property
    def all_aircraft(self) -> Iterator[Tuple[UnitType, int]]:
        """Iterates over all available aircraft types, including amounts."""
        for aircraft, count in self.inventory.items():
            if count > 0:
                yield aircraft, count

    @property
    def total_available(self) -> int:
        """Returns the total number of aircraft available."""
        # TODO: Remove?
        # This probably isn't actually useful. It's used by the AI flight
        # planner to determine how many flights of a given type it should
        # allocate, but it should probably be making that decision based on the
        # number of aircraft available to perform a particular role.
        return sum(self.inventory.values())

    def clear(self) -> None:
        """Clears all aircraft from the inventory."""
        self.inventory.clear()


class GlobalAircraftInventory:
    """Game-wide aircraft inventory."""
    def __init__(self, control_points: Iterable[ControlPoint]) -> None:
        self.inventories: Dict[ControlPoint, ControlPointAircraftInventory] = {
            cp: ControlPointAircraftInventory(cp) for cp in control_points
        }

    def reset(self) -> None:
        """Clears all control points and their inventories."""
        for inventory in self.inventories.values():
            inventory.clear()

    def set_from_control_point(self, control_point: ControlPoint) -> None:
        """Set the control point's aircraft inventory.

        If the inventory for the given control point has already been set for
        the turn, it will be overwritten.
        """
        inventory = self.inventories[control_point]
        for aircraft, count in control_point.base.aircraft.items():
            inventory.add_aircraft(aircraft, count)

    def for_control_point(
            self,
            control_point: ControlPoint) -> ControlPointAircraftInventory:
        """Returns the inventory specific to the given control point."""
        return self.inventories[control_point]

    @property
    def available_types_for_player(self) -> Iterator[UnitType]:
        """Iterates over all aircraft types available to the player."""
        seen: Set[UnitType] = set()
        for control_point, inventory in self.inventories.items():
            if control_point.captured:
                for aircraft in inventory.types_available:
                    if aircraft not in seen:
                        seen.add(aircraft)
                        yield aircraft

    def claim_for_flight(self, flight: Flight) -> None:
        """Removes aircraft from the inventory for the given flight."""
        inventory = self.for_control_point(flight.from_cp)
        inventory.remove_aircraft(flight.unit_type, flight.count)

    def return_from_flight(self, flight: Flight) -> None:
        """Returns a flight's aircraft to the inventory."""
        inventory = self.for_control_point(flight.from_cp)
        inventory.add_aircraft(flight.unit_type, flight.count)
