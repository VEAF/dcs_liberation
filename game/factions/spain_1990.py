from dcs.planes import (
    AV8BNA,
    C_101CC,
    C_130,
    E_3A,
    FA_18C_hornet,
    F_5E_3,
    KC130,
    KC_135,
)
from dcs.ships import (
    Armed_speedboat,
    CVN_74_John_C__Stennis,
    LHA_1_Tarawa,
    Oliver_Hazzard_Perry_class,
    Ticonderoga_class,
)
from dcs.vehicles import (
    AirDefence,
    Armor,
    Infantry,
    Unarmed,
)

Spain_1990 = {
    "country": "Spain",
    "side": "blue",
    "units": [
        FA_18C_hornet,
        AV8BNA,
        F_5E_3,
        C_101CC,

        KC_135,
        KC130,
        C_130,
        E_3A,

        Armor.MBT_M60A3_Patton,
        Armor.MBT_Leopard_2,
        Armor.APC_M113,

        Unarmed.Transport_M818,
        Infantry.Infantry_M4,
        Infantry.Soldier_M249,

        AirDefence.SAM_Hawk_PCP,
        AirDefence.SAM_Avenger_M1097,

        CVN_74_John_C__Stennis,
        LHA_1_Tarawa,
        Armed_speedboat,
    ], "shorad":[
        AirDefence.SAM_Avenger_M1097,
    ], "aircraft_carrier": [
        CVN_74_John_C__Stennis, # Standing as Principe de Asturias
    ], "helicopter_carrier": [
        LHA_1_Tarawa, # Standing as Juan Carlos
    ], "destroyer": [
        Oliver_Hazzard_Perry_class,
    ], "cruiser": [
        Ticonderoga_class,
    ], "carrier_names": [
        "Principe de Asturias",
    ], "lhanames": [
        "Juan Carlos I",
    ], "boat":[
        "OliverHazardPerryGroupGenerator"
    ], "has_jtac": True
}