# Content file for build_resume_pdfs.py.
# FICTIONAL EXAMPLE: Alex Rivera, every employer and number here is invented.
# Copy this file to a scratch folder, replace the text with the approved tailored text, and run the script.
# Keep wording verbatim from the master resume except for the changes the user approved in chat.

NAME = "Alex Rivera"
CONTACT = "alex@example.com / (555) 010-0100 / linkedin.com/in/example"

# Optional settings
ACCENT = "#3b6f8f"               # rule color in the designed PDF
TARGET_PAGES = 1                  # the script flags any other page count (use 2 for a full resume)
EXTRA_SECTION_TITLE = "Additional Information"

# The summary is split so the first phrase can be bold in the designed PDF.
SUMMARY_LEAD = "Support operations leader"
SUMMARY_REST = (
    " with 10+ years running teams of 6 to 14. Owned first response time and CSAT at Orchard Systems, "
    "and built the escalation process at Larkfield Software. Works from the numbers and keeps the method "
    "open to inspection."
)

SKILLS = [
    "Support Operations",
    "Quality & CSAT Reporting",
    "Escalation Design",
    "Staffing & Scheduling",
    "Helpdesk Configuration",
    "Team Leadership",
]

# One dict per job, newest first. A company with several titles lists them all in `titles`.
# `ats_titles` is optional: (title, company, dates) triples, one per line in the ATS PDF.
# Without it, the ATS PDF derives the lines from `titles` and `company`.
ROLES = [
    {
        "company": "Orchard Systems",
        "titles": [("Director of Support Operations", "2021 - 2024")],
        "intro": "Led a team of 14 with a $2.2M budget, reporting to the VP of Customer Experience.",
        "bullets": [
            "Cut median first response time on email from 9 hours to 3 in 2022",
            "Raised CSAT on rated tickets from 84% to 91% over 2022 and 2023",
        ],
    },
    {
        "company": "Larkfield Software",
        "titles": [
            ("Support Manager", "2019 - 2021"),
            ("Previous: Senior Support Agent", "2018 - 2019"),
        ],
        "ats_titles": [
            ("Support Manager", "Larkfield Software", "2019 - 2021"),
            ("Senior Support Agent", "Larkfield Software", "2018 - 2019"),
        ],
        "intro": "Led a team of 6, reporting to the head of support.",
        "bullets": [
            "Built the escalation process; escalations that missed their window fell from 31% to 9% in the first year",
        ],
    },
]

# Older or shorter roles, one paragraph each. `name` prints in bold in the designed PDF.
EARLIER = [
    {"name": "Brightside Retail", "rest": ", Denver, CO | Customer Care Lead, 2015 - 2018. Ran the weekend support shift."},
]

# (bold part, rest) pairs
EDUCATION = [
    ("Bachelor of Arts,", " University of Colorado"),
]

# Extra lines under the extra section title. Use an empty list to leave the section out.
ADDITIONAL = [
    "Volunteer coordinator, Front Range Food Bank - 2020 to present",
]
