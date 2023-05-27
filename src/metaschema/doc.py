# generated by datamodel-codegen:
#   filename:  doc.json
#   timestamp: 2023-05-27T20:43:24+00:00

from __future__ import annotations

from typing import Any, Dict, List

from pydantic import BaseModel, Field


class Producer(BaseModel):
    name: str = Field(None, description="")
    abbr: str = Field(None, description="")
    affiliation: str = Field(None, description="")
    role: str = Field(None, description="")


class MetadataInformation(BaseModel):
    title: str
    idno: str
    producers: List[Producer]
    production_date: str
    version: str


class TitleStatement(BaseModel):
    idno: str
    title: str
    sub_title: str
    alternate_title: str
    translated_title: str


class AuthorIdItem(BaseModel):
    type: None
    id: None


class Author(BaseModel):
    first_name: str
    initial: str
    last_name: str
    affiliation: str
    author_id: List[AuthorIdItem]
    full_name: str


class Editor(BaseModel):
    first_name: str
    initial: str
    last_name: str
    affiliation: str


class Identifier(BaseModel):
    type: str
    identifier: str


class TocStructuredItem(BaseModel):
    id: str
    parent_id: str
    name: str


class Note(BaseModel):
    note: str


class RefCountryItem(BaseModel):
    name: str
    code: str


class GeographicUnit(BaseModel):
    name: str
    code: str
    type: str


class BboxItem(BaseModel):
    west: str
    east: str
    south: str
    north: str


class Language(BaseModel):
    name: str
    code: str


class LicenseItem(BaseModel):
    name: str
    uri: str


class BibliographicCitationItem(BaseModel):
    style: str
    citation: str


class Translator(BaseModel):
    first_name: str
    initial: str
    last_name: str
    affiliation: str


class Contributor(BaseModel):
    first_name: str
    initial: str
    last_name: str
    affiliation: str
    contribution: str


class Contact(BaseModel):
    name: str
    role: str
    affiliation: str
    email: str
    telephone: str
    uri: str


class Source(BaseModel):
    source_origin: str
    source_char: str
    source_doc: str


class DataSource(BaseModel):
    name: str
    uri: str
    note: str


class Keyword(BaseModel):
    name: str
    vocabulary: str
    uri: str


class Theme(BaseModel):
    id: str
    name: str
    parent_id: str
    vocabulary: str
    uri: str


class Topic(BaseModel):
    id: str
    name: str
    parent_id: str
    vocabulary: str
    uri: str


class Discipline(BaseModel):
    id: str
    name: str
    parent_id: str
    vocabulary: str
    uri: str


class Relation(BaseModel):
    name: str
    type: str


class Link(BaseModel):
    uri: str
    description: str


class Reproducibility(BaseModel):
    statement: str
    links: List[Link]


class DocumentDescription(BaseModel):
    title_statement: TitleStatement = Field(..., description="")
    authors: List[Author] = Field(None, description="")
    editors: List[Editor] = Field(None, description="")
    date_created: str = Field(None, description="")
    date_available: str = Field(None, description="")
    date_modified: str = Field(None, description="")
    date_published: str = Field(None, description="")
    identifiers: List[Identifier] = Field(None, description="")
    type: str = Field(None, description="")
    status: str = Field(None, description="")
    description: str = Field(None, description="")
    toc: str = Field(None, description="")
    toc_structured: List[TocStructuredItem] = Field(None, description="")
    abstract: str = Field(None, description="")
    notes: List[Note] = Field(None, description="")
    scope: str = Field(None, description="")
    ref_country: List[RefCountryItem] = Field(None, description="")
    geographic_units: List[GeographicUnit] = Field(None, description="")
    bbox: List[BboxItem] = Field(None, description="")
    spatial_coverage: str = Field(None, description="")
    temporal_coverage: str = Field(None, description="")
    publication_frequency: str = Field(None, description="")
    languages: List[Language] = Field(None, description="")
    license: List[LicenseItem] = Field(None, description="")
    bibliographic_citation: List[BibliographicCitationItem] = Field(None, description="")
    chapter: str = Field(None, description="")
    edition: str = Field(None, description="")
    institution: str = Field(None, description="")
    journal: str = Field(None, description="")
    volume: str = Field(None, description="")
    number: str = Field(None, description="")
    pages: str = Field(None, description="")
    series: str = Field(None, description="")
    publisher: str = Field(None, description="")
    publisher_address: str = Field(None, description="")
    annote: str = Field(None, description="")
    booktitle: str = Field(None, description="")
    crossref: str = Field(None, description="")
    howpublished: str = Field(None, description="")
    key: str = Field(None, description="")
    organization: str = Field(None, description="")
    url: str = Field(None, description="")
    translators: List[Translator] = Field(None, description="")
    contributors: List[Contributor] = Field(None, description="")
    contacts: List[Contact] = Field(None, description="")
    rights: str = Field(None, description="")
    copyright: str = Field(None, description="")
    usage_terms: str = Field(None, description="")
    disclaimer: str = Field(None, description="")
    security_classification: str = Field(None, description="")
    access_restrictions: str = Field(None, description="")
    sources: List[Source] = Field(None, description="")
    data_sources: List[DataSource] = Field(None, description="")
    keywords: List[Keyword] = Field(None, description="")
    themes: List[Theme] = Field(None, description="")
    topics: List[Topic] = Field(None, description="")
    disciplines: List[Discipline] = Field(None, description="")
    audience: str = Field(None, description="")
    mandate: str = Field(None, description="")
    pricing: str = Field(None, description="")
    relations: List[Relation] = Field(None, description="")
    reproducibility: Reproducibility = Field(None, description="")


class OriginDescription(BaseModel):
    harvest_date: str
    altered: bool
    base_url: str
    identifier: str
    date_stamp: str
    metadata_namespace: str


class ProvenanceItem(BaseModel):
    origin_description: OriginDescription


class Tag(BaseModel):
    tag: str
    tag_group: str


class ModelInfoItem(BaseModel):
    source: str
    author: str
    version: str
    model_id: str
    nb_topics: int
    description: str
    corpus: str
    uri: str


class TopicWord(BaseModel):
    word: str
    word_weight: int


class TopicDescriptionItem(BaseModel):
    topic_id: None
    topic_score: None
    topic_label: str
    topic_words: List[TopicWord]


class LdaTopic(BaseModel):
    model_info: List[ModelInfoItem]
    topic_description: List[TopicDescriptionItem]


class Embedding(BaseModel):
    id: str
    description: str
    date: str
    vector: None


class Model(BaseModel):
    repositoryid: str
    published: int
    overwrite: str
    metadata_information: MetadataInformation
    document_description: DocumentDescription
    provenance: List[ProvenanceItem]
    tags: List[Tag]
    lda_topics: List[LdaTopic]
    embeddings: List[Embedding]
    additional: Dict[str, Any]
