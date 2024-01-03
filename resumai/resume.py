from dataclasses import dataclass
from typing import Optional
from serde.toml import from_toml


@dataclass
class ContactInfo:
    first_name: str
    last_name: str
    phone: str
    email: str
    linkedin: Optional[str]
    github: Optional[str]
    website: Optional[str]


@dataclass
class Degree:
    degree: str
    institution: str
    year: Optional[int]
    gpa: Optional[float]


@dataclass
class Job:
    employer: str
    title: str
    start_date: str
    end_date: Optional[str]
    description: Optional[list[str]]


@dataclass
class Resume:
    contact_info: ContactInfo
    skills: Optional[dict[str, list[str]]]
    education: Optional[list[Degree]]
    narrative: Optional[str]
    job_history: list[Job]


def read_resume(path: str="resume.toml") -> Resume:
    with open(path, "r") as f:
        return from_toml(Resume, f.read())
