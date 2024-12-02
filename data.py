from datetime import date

from data_types import PersonalStuff, WorkEntry


personal_stuff: PersonalStuff = PersonalStuff(
    first_name="Thomas",
    middle_name="Jaroslaw",
    last_name="Kosciuch",
    address="30 Shore Breeze Dr., Toronto, ON",
    email="thomas@kosciuch.ca",
)

work_entries: list[WorkEntry] = [
    WorkEntry(
        name="Quintessence Wealth",
        position="Tech Lead",
        start_date=date(2025, 1, 1),
        end_date=date.max,
        location="Toronto, On., Canada",
        bullets=[
            ("Drive direction of technology on the team", 1),
            ("Responsible hiring", 1),

        ],
        tools=[],
    ),
    WorkEntry(
        name="Quintessence Wealth",
        position="Staff Engineer",
        start_date=date(2023, 4, 1),
        end_date=date(2025, 1, 1),
        location="Toronto, On., Canada",
        bullets=[
            # compliance
            # trade alerts
            # algo trading tools
            ("Responsible for the success of 100M of daily trades; availability of all previous days’ trades (TSX and NYSE); and the real-time transaction data of our customers", 3),
            ("Plan, and implement and/or delegate features, infrastructure, and products  with org-wide impact", 2),
            ("Mentor underperforming engineers to achieve outstanding performance evaluations through mentorship", 2),
            ("Lead integration of observability platforms", 1),
        ],
        tools=[],
    ),
    WorkEntry(
        name="Quintessence Wealth",
        position="Senior Software Engineer",
        start_date=date(2023, 4, 1),
        end_date=date(2022, 2, 1),
        location="Toronto, On., Canada",
        bullets=[
            ("Adopted modern technologies to help with reliability (infrastructure as code via CDK; error monitoring APIs; feature flags), error reporting (Sentry), and built frameworks for unit- and integration tests", 4),
            ("Designed and implemented integrations (Docusign, Salesforce, Flinx, Conquest, Canada Post, D1G1T, MX, National Bank Independant Network)", 2),
        ],
        tools=[],
    ),
    WorkEntry(
        name="Adaptavist Inc.",
        position="Software Engineer (Cloud)",
        start_date=date(2020, 7, 1),
        end_date=date(2022, 2, 1),
        location="Toronto, On., Canada",
        bullets=[
            ("Scaled internal tooling to support large scale operations", 1),
            ("Mentored junior engineers and interns", 1),
        ],
        tools=[],
    ),
    WorkEntry(
        name="Jam Direct Inc.",
        position="Software Engineer",
        start_date=date(2019, 5, 1),
        end_date=date(2020, 7, 1),
        location="Toronto, On., Canada",
        bullets=[],
        tools=[],
    ),
    WorkEntry(
        name="University of Toronto",
        position="Research Fellow",
        start_date=date(2019, 5, 1),
        end_date=date(2020, 7, 1),
        location="Toronto, On., Canada",
        bullets=[],
        tools=[],
    ),
]
