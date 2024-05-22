from intranet_trems import _
from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel import model
from plone.supermodel.model import Schema
from zope import schema
from zope.interface import implementer

import re


def is_valid_email(value: str) -> bool:
    """Validar se o email é @tre-ms.jus.br."""
    return value.endswith("@tre-ms.jus.br") if value else True


def is_valid_extension(value: str) -> bool:
    """Validar se o o ramal tem 4 dígitos numéricos."""
    return re.match(r"^\d{4}$", value) if value else True


class IArea(Schema):
    """Definição de uma área no TRE-MS."""

    title = schema.TextLine(title=_("Nome Completo"), required=True)
    description = schema.Text(title=_("Biografia"), required=False)

    model.fieldset(
        "contato",
        _("Contato"),
        fields=[
            "email",
            "ramal",
        ],
    )
    email = Email(
        title=_("Email"),
        required=True,
        constraint=is_valid_email,
    )
    ramal = schema.TextLine(
        title=("Ramal"),
        required=True,
        constraint=is_valid_extension,
    )


@implementer(IArea)
class Area(Container):
    """Uma área no TRE-MS."""
