# SEO Audit Flow - CrewAI Flow

## 🚀 Overview

This flow enables users to perform SEO audits on individual webpages by leveraging a team of specialized AI agents that collaborate to analyze HTML content and provide actionable recommendations.

## ✨ Key Features

- **Automated Content Fetching**: Retrieves HTML content from any URL for analysis
- **On-Page SEO Analysis**: Identifies critical on-page elements like title tags, meta descriptions, and heading structure
- **Actionable Reporting**: Generates comprehensive reports with clear recommendations for improvement

## 🔍 Use Cases

This flow is ideal for:

- Website owners wanting to quickly audit individual pages
- SEO professionals needing a starting point for deeper analysis
- Content creators checking SEO elements before publishing

## 🛠️ Requirements

- CrewAI version: 0.108.0
- API Keys needed:
    - LLM Provider (OpenAI, Anthropic, Google) if not using local models.
- Additional dependencies: requests

## 📊 Example Output

The flow generates a detailed markdown report containing:

```
# SEO Audit Report for example.com

## Overview
The page has a properly structured title tag and meta description, but lacks sufficient heading structure.

## Title Tag
Title: "Example Domain" (45 characters)
✅ Present and within optimal length (under 60 characters)

## Meta Description
Description: "This domain is for use in illustrative examples in documents." (64 characters)
✅ Present but slightly short (optimal length 120-160 characters)

## Heading Structure
❌ Missing H1 tag
❌ No clear heading hierarchy

## Recommendations
1. Add a clear H1 tag that matches search intent
2. Develop a logical heading structure (H2, H3, etc.)
3. Expand the meta description to include keywords and a call to action
```

## 📚 Resources and References

- [CrewAI Documentation](https://docs.crewai.com/)
- [SEO Best Practices](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)

## Usage

To run the SEO audit flow:

```
python -m seo_audit_flow.main "https://example.com"
```

## 🤝 Contributing

[Optional: Include information about how others can contribute to your flow]

## 📝 License

[Specify the license for your flow]