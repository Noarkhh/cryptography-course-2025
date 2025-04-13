from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from xsdata.models.datatype import XmlDateTime


@dataclass
class Identifier:
    class Meta:
        namespace = (
            "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001"
        )

    type_value: Optional[QName] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
        },
    )
    identifier: Optional[int] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )


@dataclass
class EncryptionAlgorithmData:
    class Meta:
        namespace = (
            "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001"
        )

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Element",
            "required": True,
        },
    )
    mode: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mode",
            "type": "Element",
            "required": True,
        },
    )
    padding: Optional[str] = field(
        default=None,
        metadata={
            "name": "Padding",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class EncryptionAlgorithmKey:
    class Meta:
        namespace = (
            "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001"
        )

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Element",
            "required": True,
        },
    )
    mode: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mode",
            "type": "Element",
            "required": True,
        },
    )
    padding: Optional[str] = field(
        default=None,
        metadata={
            "name": "Padding",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class EncryptionInitializationVector:
    class Meta:
        namespace = (
            "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001"
        )

    encoding: Optional[str] = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Element",
            "required": True,
        },
    )
    bytes: Optional[int] = field(
        default=None,
        metadata={
            "name": "Bytes",
            "type": "Element",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class EncryptionKey:
    class Meta:
        namespace = (
            "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001"
        )

    encoding: Optional[str] = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Element",
            "required": True,
        },
    )
    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Element",
            "required": True,
        },
    )
    size: Optional[int] = field(
        default=None,
        metadata={
            "name": "Size",
            "type": "Element",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class FormCode:
    class Meta:
        namespace = (
            "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001"
        )

    system_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SystemCode",
            "type": "Element",
            "required": True,
        },
    )
    schema_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchemaVersion",
            "type": "Element",
            "required": True,
        },
    )
    target_namespace: Optional[str] = field(
        default=None,
        metadata={
            "name": "TargetNamespace",
            "type": "Element",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DataObjectFormat:
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"

    object_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "ObjectReference",
            "type": "Attribute",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "required": True,
        },
    )
    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "MimeType",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class CanonicalizationMethod:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DigestMethod:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class RsakeyValue:
    class Meta:
        name = "RSAKeyValue"
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    modulus: Optional[str] = field(
        default=None,
        metadata={
            "name": "Modulus",
            "type": "Element",
            "required": True,
        },
    )
    exponent: Optional[str] = field(
        default=None,
        metadata={
            "name": "Exponent",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SignatureMethod:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Transform:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class X509Data:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    x509_certificate: Optional[str] = field(
        default=None,
        metadata={
            "name": "X509Certificate",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DocumentType:
    class Meta:
        namespace = (
            "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001"
        )

    service: Optional[str] = field(
        default=None,
        metadata={
            "name": "Service",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    form_code: Optional[FormCode] = field(
        default=None,
        metadata={
            "name": "FormCode",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )


@dataclass
class Encryption:
    class Meta:
        namespace = (
            "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001"
        )

    encryption_key: Optional[EncryptionKey] = field(
        default=None,
        metadata={
            "name": "EncryptionKey",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    encryption_initialization_vector: Optional[
        EncryptionInitializationVector
    ] = field(
        default=None,
        metadata={
            "name": "EncryptionInitializationVector",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    encryption_algorithm_key: Optional[EncryptionAlgorithmKey] = field(
        default=None,
        metadata={
            "name": "EncryptionAlgorithmKey",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )
    encryption_algorithm_data: Optional[EncryptionAlgorithmData] = field(
        default=None,
        metadata={
            "name": "EncryptionAlgorithmData",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001",
            "required": True,
        },
    )


@dataclass
class CertDigest:
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"

    digest_method: Optional[DigestMethod] = field(
        default=None,
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )
    digest_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )


@dataclass
class SignedDataObjectProperties:
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"

    data_object_format: Optional[DataObjectFormat] = field(
        default=None,
        metadata={
            "name": "DataObjectFormat",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class KeyValue:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    rsakey_value: Optional[RsakeyValue] = field(
        default=None,
        metadata={
            "name": "RSAKeyValue",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Transforms:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    transform: list[Transform] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Context:
    class Meta:
        namespace = "http://ksef.mf.gov.pl/schema/gtw/svc/online/auth/request/2021/10/01/0001"

    challenge: Optional[str] = field(
        default=None,
        metadata={
            "name": "Challenge",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
        },
    )
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
        },
    )
    document_type: Optional[DocumentType] = field(
        default=None,
        metadata={
            "name": "DocumentType",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
        },
    )
    encryption: Optional[Encryption] = field(
        default=None,
        metadata={
            "name": "Encryption",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001",
            "required": True,
        },
    )


@dataclass
class Cert:
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"

    cert_digest: Optional[CertDigest] = field(
        default=None,
        metadata={
            "name": "CertDigest",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class KeyInfo:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
        },
    )
    key_value: Optional[KeyValue] = field(
        default=None,
        metadata={
            "name": "KeyValue",
            "type": "Element",
            "required": True,
        },
    )
    x509_data: Optional[X509Data] = field(
        default=None,
        metadata={
            "name": "X509Data",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Reference:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    transforms: Optional[Transforms] = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    digest_method: Optional[DigestMethod] = field(
        default=None,
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "required": True,
        },
    )
    digest_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SigningCertificateV2:
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"

    cert: Optional[Cert] = field(
        default=None,
        metadata={
            "name": "Cert",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SignedInfo:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    canonicalization_method: Optional[CanonicalizationMethod] = field(
        default=None,
        metadata={
            "name": "CanonicalizationMethod",
            "type": "Element",
            "required": True,
        },
    )
    signature_method: Optional[SignatureMethod] = field(
        default=None,
        metadata={
            "name": "SignatureMethod",
            "type": "Element",
            "required": True,
        },
    )
    reference: list[Reference] = field(
        default_factory=list,
        metadata={
            "name": "Reference",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class SignedSignatureProperties:
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"

    signing_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SigningTime",
            "type": "Element",
            "required": True,
        },
    )
    signing_certificate_v2: Optional[SigningCertificateV2] = field(
        default=None,
        metadata={
            "name": "SigningCertificateV2",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SignedProperties:
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
        },
    )
    signed_signature_properties: Optional[SignedSignatureProperties] = field(
        default=None,
        metadata={
            "name": "SignedSignatureProperties",
            "type": "Element",
            "required": True,
        },
    )
    signed_data_object_properties: Optional[SignedDataObjectProperties] = (
        field(
            default=None,
            metadata={
                "name": "SignedDataObjectProperties",
                "type": "Element",
                "required": True,
            },
        )
    )


@dataclass
class QualifyingProperties:
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"

    target: Optional[str] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Attribute",
            "required": True,
        },
    )
    signed_properties: Optional[SignedProperties] = field(
        default=None,
        metadata={
            "name": "SignedProperties",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Object:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    qualifying_properties: Optional[QualifyingProperties] = field(
        default=None,
        metadata={
            "name": "QualifyingProperties",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )


@dataclass
class Signature:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
        },
    )
    signed_info: Optional[SignedInfo] = field(
        default=None,
        metadata={
            "name": "SignedInfo",
            "type": "Element",
            "required": True,
        },
    )
    signature_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignatureValue",
            "type": "Element",
            "required": True,
        },
    )
    key_info: Optional[KeyInfo] = field(
        default=None,
        metadata={
            "name": "KeyInfo",
            "type": "Element",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "Object",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class InitSessionSignedRequest:
    class Meta:
        namespace = "http://ksef.mf.gov.pl/schema/gtw/svc/online/auth/request/2021/10/01/0001"

    context: Optional[Context] = field(
        default=None,
        metadata={
            "name": "Context",
            "type": "Element",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
