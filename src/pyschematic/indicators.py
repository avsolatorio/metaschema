from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Topic(BaseModel):
    name: str
    vocabulary: str


class TimePeriod(BaseModel):
    start: str
    end: str


class GeographicUnit(BaseModel):
    name: str
    code: str


class LicenseItem(BaseModel):
    name: str
    uri: str


class Link(BaseModel):
    type: str
    description: str
    uri: str


class ApiDocumentationItem(BaseModel):
    description: str
    uri: str


class Source(BaseModel):
    name: str


class Note(BaseModel):
    note: str


class Producer(BaseModel):
    name: str
    abbr: str
    affiliation: str
    role: str


class MetadataCreation(BaseModel):
    producers: Optional[List[Producer]] = None
    prod_date: Optional[datetime.date] = None
    version: Optional[str] = None


class SeriesDescription(BaseModel):
    idno: str
    doi: str
    name: str
    database_id: str
    measurement_unit: str
    periodicity: str
    base_period: str
    definition_short: str
    definition_long: str
    methodology: str
    limitation: str
    topics: List[Topic]
    relevance: str
    time_periods: List[TimePeriod]
    geographic_units: List[GeographicUnit]
    aggregation_method: str
    license: List[LicenseItem]
    links: List[Link]
    api_documentation: List[ApiDocumentationItem]
    sources: List[Source]
    sources_note: str
    keywords: List
    notes: List[Note]


class Indicators(BaseModel):
    metadata_creation: Optional[MetadataCreation] = None
    series_description: SeriesDescription
    schematype: str
