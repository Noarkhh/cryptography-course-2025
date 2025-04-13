from dataclasses import dataclass, field
from typing import Optional

from generated.online.types.pkg_2021.pkg_10.pkg_01.pkg_0001.online_types import (
    AuthorisationContextTokenType,
)

__NAMESPACE__ = (
    "http://ksef.mf.gov.pl/schema/gtw/svc/online/auth/request/2021/10/01/0001"
)


@dataclass
class RegisterAccessPointProviderRequest:
    class Meta:
        namespace = "http://ksef.mf.gov.pl/schema/gtw/svc/online/auth/request/2021/10/01/0001"

    name_app: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameAPP",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 64,
        },
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 64,
        },
    )


@dataclass
class InitSessionTokenRequest:
    class Meta:
        namespace = "http://ksef.mf.gov.pl/schema/gtw/svc/online/auth/request/2021/10/01/0001"

    context: Optional[AuthorisationContextTokenType] = field(
        default=None,
        metadata={
            "name": "Context",
            "type": "Element",
            "required": True,
        },
    )
