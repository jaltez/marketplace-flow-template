#!/usr/bin/env python
import os
from pydantic import BaseModel

from crewai.flow import Flow, listen, start
from seo_audit_flow.crews.seo_crew.seo_crew import SeoCrew

class SeoAuditState(BaseModel):
    url: str = ""
    audit_report: str = ""

class SeoAuditFlow(Flow[SeoAuditState]):

    @start()
    def run_seo_audit(self):
        print("Running SEO audit for ", self.state.url)

        result = (
            SeoCrew()
            .crew()
            .kickoff(inputs={"url": self.state.url})
        )

        print("SEO audit completed")
        self.state.audit_report = result.raw

    @listen(run_seo_audit)
    def save_report(self):
        print("Saving SEO audit report")
        print(f"Report saved to seo_audit_report.md")


def kickoff():
    """Run the SEO audit flow with the provided URL or from environment variable."""

    url = os.getenv("SEO_AUDIT_URL", "")
        
    if not url:
        raise ValueError("URL is required")
        
    print(f"Starting SEO audit for: {url}")
    seo_flow = SeoAuditFlow()
    seo_flow.state.url = url
    seo_flow.kickoff()
    return seo_flow.state.audit_report


def plot():
    seo_flow = SeoAuditFlow()
    seo_flow.plot()


if __name__ == "__main__":
    kickoff()
