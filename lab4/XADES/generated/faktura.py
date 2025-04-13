from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "http://crd.gov.pl/wzor/2023/06/29/12648/"


@dataclass
class Adres:
    class Meta:
        namespace = "http://crd.gov.pl/wzor/2023/06/29/12648/"

    kod_kraju: Optional[str] = field(
        default=None,
        metadata={
            "name": "KodKraju",
            "type": "Element",
            "required": True,
        },
    )
    adres_l1: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdresL1",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DaneIdentyfikacyjne:
    class Meta:
        namespace = "http://crd.gov.pl/wzor/2023/06/29/12648/"

    nip: Optional[int] = field(
        default=None,
        metadata={
            "name": "NIP",
            "type": "Element",
            "required": True,
        },
    )
    nazwa: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nazwa",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class KodFormularza:
    class Meta:
        namespace = "http://crd.gov.pl/wzor/2023/06/29/12648/"

    kod_systemowy: Optional[str] = field(
        default=None,
        metadata={
            "name": "kodSystemowy",
            "type": "Attribute",
            "required": True,
        },
    )
    wersja_schemy: Optional[str] = field(
        default=None,
        metadata={
            "name": "wersjaSchemy",
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class NoweSrodkiTransportu:
    class Meta:
        namespace = "http://crd.gov.pl/wzor/2023/06/29/12648/"

    p_22_n: Optional[int] = field(
        default=None,
        metadata={
            "name": "P_22N",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Pmarzy:
    class Meta:
        name = "PMarzy"
        namespace = "http://crd.gov.pl/wzor/2023/06/29/12648/"

    p_pmarzy_n: Optional[int] = field(
        default=None,
        metadata={
            "name": "P_PMarzyN",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Zwolnienie:
    class Meta:
        namespace = "http://crd.gov.pl/wzor/2023/06/29/12648/"

    p_19_n: Optional[int] = field(
        default=None,
        metadata={
            "name": "P_19N",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Adnotacje:
    class Meta:
        namespace = "http://crd.gov.pl/wzor/2023/06/29/12648/"

    p_16: Optional[int] = field(
        default=None,
        metadata={
            "name": "P_16",
            "type": "Element",
            "required": True,
        },
    )
    p_17: Optional[int] = field(
        default=None,
        metadata={
            "name": "P_17",
            "type": "Element",
            "required": True,
        },
    )
    p_18: Optional[int] = field(
        default=None,
        metadata={
            "name": "P_18",
            "type": "Element",
            "required": True,
        },
    )
    p_18_a: Optional[int] = field(
        default=None,
        metadata={
            "name": "P_18A",
            "type": "Element",
            "required": True,
        },
    )
    zwolnienie: Optional[Zwolnienie] = field(
        default=None,
        metadata={
            "name": "Zwolnienie",
            "type": "Element",
            "required": True,
        },
    )
    nowe_srodki_transportu: Optional[NoweSrodkiTransportu] = field(
        default=None,
        metadata={
            "name": "NoweSrodkiTransportu",
            "type": "Element",
            "required": True,
        },
    )
    p_23: Optional[int] = field(
        default=None,
        metadata={
            "name": "P_23",
            "type": "Element",
            "required": True,
        },
    )
    pmarzy: Optional[Pmarzy] = field(
        default=None,
        metadata={
            "name": "PMarzy",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Naglowek:
    class Meta:
        namespace = "http://crd.gov.pl/wzor/2023/06/29/12648/"

    kod_formularza: Optional[KodFormularza] = field(
        default=None,
        metadata={
            "name": "KodFormularza",
            "type": "Element",
            "required": True,
        },
    )
    wariant_formularza: Optional[int] = field(
        default=None,
        metadata={
            "name": "WariantFormularza",
            "type": "Element",
            "required": True,
        },
    )
    data_wytworzenia_fa: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataWytworzeniaFa",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Podmiot1:
    class Meta:
        namespace = "http://crd.gov.pl/wzor/2023/06/29/12648/"

    dane_identyfikacyjne: Optional[DaneIdentyfikacyjne] = field(
        default=None,
        metadata={
            "name": "DaneIdentyfikacyjne",
            "type": "Element",
            "required": True,
        },
    )
    adres: Optional[Adres] = field(
        default=None,
        metadata={
            "name": "Adres",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Podmiot2:
    class Meta:
        namespace = "http://crd.gov.pl/wzor/2023/06/29/12648/"

    dane_identyfikacyjne: Optional[DaneIdentyfikacyjne] = field(
        default=None,
        metadata={
            "name": "DaneIdentyfikacyjne",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Fa:
    class Meta:
        namespace = "http://crd.gov.pl/wzor/2023/06/29/12648/"

    kod_waluty: Optional[str] = field(
        default=None,
        metadata={
            "name": "KodWaluty",
            "type": "Element",
            "required": True,
        },
    )
    p_1: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "P_1",
            "type": "Element",
            "required": True,
        },
    )
    p_2: Optional[str] = field(
        default=None,
        metadata={
            "name": "P_2",
            "type": "Element",
            "required": True,
        },
    )
    p_15: Optional[float] = field(
        default=None,
        metadata={
            "name": "P_15",
            "type": "Element",
            "required": True,
        },
    )
    adnotacje: Optional[Adnotacje] = field(
        default=None,
        metadata={
            "name": "Adnotacje",
            "type": "Element",
            "required": True,
        },
    )
    rodzaj_faktury: Optional[str] = field(
        default=None,
        metadata={
            "name": "RodzajFaktury",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Faktura:
    class Meta:
        namespace = "http://crd.gov.pl/wzor/2023/06/29/12648/"

    naglowek: Optional[Naglowek] = field(
        default=None,
        metadata={
            "name": "Naglowek",
            "type": "Element",
            "required": True,
        },
    )
    podmiot1: Optional[Podmiot1] = field(
        default=None,
        metadata={
            "name": "Podmiot1",
            "type": "Element",
            "required": True,
        },
    )
    podmiot2: Optional[Podmiot2] = field(
        default=None,
        metadata={
            "name": "Podmiot2",
            "type": "Element",
            "required": True,
        },
    )
    fa: Optional[Fa] = field(
        default=None,
        metadata={
            "name": "Fa",
            "type": "Element",
            "required": True,
        },
    )
