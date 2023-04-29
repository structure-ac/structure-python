"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class Company:
    r"""returns the company"""
    
    about: str = dataclasses.field()
    r"""The company's description"""
    affiliated: list[str] = dataclasses.field()
    r"""Affiliated companies to the company"""
    company_size: str = dataclasses.field()
    r"""The size of the company"""
    country_code: str = dataclasses.field()
    r"""The country's country code"""
    employees: list[str] = dataclasses.field()
    r"""A sample of the company's employees. See the employees endpoint for the full list."""
    employees_in_linkedin: float = dataclasses.field()
    r"""The number of company employees on LinkedIn"""
    followers: float = dataclasses.field()
    r"""The number of company followers on LinkedIn"""
    founded: float = dataclasses.field()
    r"""The year the company was founded"""
    funding: str = dataclasses.field()
    r"""The funding status of the company"""
    headquarters: str = dataclasses.field()
    r"""The country's headquarters"""
    id: float = dataclasses.field()
    r"""The key for looking up the company"""
    industries: str = dataclasses.field()
    r"""The company's industries"""
    investors: str = dataclasses.field()
    r"""The company's investors"""
    jobs: list[str] = dataclasses.field()
    r"""Sample of company's Jobs. See the jobs endpoint for the full list."""
    lid: str = dataclasses.field()
    r"""The company's LinkedIn ID"""
    locations: list[str] = dataclasses.field()
    r"""The company's locations"""
    logo: str = dataclasses.field()
    r"""URL to the company's logo"""
    name: str = dataclasses.field()
    r"""The company's name"""
    organization_type: str = dataclasses.field()
    r"""The type of organization"""
    profiles: list[str] = dataclasses.field()
    r"""The company's profiles"""
    region: str = dataclasses.field()
    r"""The comapny's headquarters region"""
    similar: list[str] = dataclasses.field()
    r"""Similar companies to this company"""
    slogan: str = dataclasses.field()
    r"""The company's slogan"""
    specialities: str = dataclasses.field()
    r"""The company's specialities"""
    sphere: str = dataclasses.field()
    r"""The company's sphere of products"""
    type: str = dataclasses.field()
    r"""The type of company (public, private, etc.)"""
    url: str = dataclasses.field()
    r"""The company's linkedIn URL"""
    website: str = dataclasses.field()
    r"""The company's website"""
    