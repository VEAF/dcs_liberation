from dcs.helicopters import (
    Mi_24V,
    Mi_28N,
)
from dcs.planes import (
    A_50,
    An_26B,
    An_30M,
    F_14B,
    F_4E,
    F_5E_3,
    IL_76MD,
    IL_78M,
    MiG_21Bis,
    MiG_29A,
    Su_17M4,
    Su_24M,
    Su_25,
    Yak_40,
)
from dcs.ships import (
    Bulk_cargo_ship_Yakushev,
    CV_1143_5_Admiral_Kuznetsov,
    Dry_cargo_ship_Ivanov,
    Tanker_Elnya_160,
)
from dcs.vehicles import (
    AirDefence,
    Armor,
    Infantry,
    Unarmed,
)

Iran_2015 = {
    "country": "Iran",
    "side": "red",
    "units": [

        MiG_29A,
        F_4E,
        F_14B,
        F_5E_3,

        MiG_21Bis,
        Su_24M,
        Su_25,
        Su_17M4,

        IL_76MD,
        IL_78M,
        An_26B,
        An_30M,
        Yak_40,

        A_50,

        Mi_28N,
        Mi_24V,

        AirDefence.SAM_Hawk_PCP,
        AirDefence.SAM_SA_2_LN_SM_90,
        AirDefence.SAM_SA_6_Kub_LN_2P25,
        AirDefence.HQ_7_Self_Propelled_LN,
        AirDefence.SAM_SA_11_Buk_LN_9A310M1,

        Armor.APC_M113,
        Armor.APC_BTR_80,
        Armor.MBT_M60A3_Patton,
        Armor.MBT_T_72B,

        Unarmed.Transport_Ural_375,
        Unarmed.Transport_UAZ_469,
        Infantry.Soldier_AK,

        CV_1143_5_Admiral_Kuznetsov,
        Bulk_cargo_ship_Yakushev,
        Dry_cargo_ship_Ivanov,
        Tanker_Elnya_160
    ],
    "shorad":[
        AirDefence.HQ_7_Self_Propelled_LN,
        AirDefence.AAA_ZU_23_Insurgent_Closed
    ], "boat":[
        "GrishaGroupGenerator", "MolniyaGroupGenerator", "KiloSubGroupGenerator"
    ]
}