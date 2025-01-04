from datetime import date
from typing import List

from data_types import PersonalStuff, WorkEntry, SubCategory, SkillCategory


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
            ("- Drive direction of technology on the team", 1),
            ("- Responsible hiring", 1),

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
            ("- Ensured the success of 100M in daily trades by maintaining the availability of all previous days’ trades across TSX and NYSE.", 2),
            ("- Developed and maintained advanced algorithmic trading tools, enabling high-speed, data-driven trading decisions.", 2),
            ("- Built real-time trade alert systems to enhance market responsiveness and operational efficiency.", 2),
            ("- Designed and deployed compliance tools, improving adherence to regulatory requirements and audit readiness.", 2),
            ("- Built real-time trade alert systems to enhance market responsiveness and operational efficiency.", 2),
            ("- Mentored underperforming engineers, resulting in significant improvements in technical skills and performance evaluations.", 2),
            ("- Led by example, fostering a collaborative and growth-focused engineering culture.", 2),
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
            ("- Adopted modern technologies to help with reliability (infrastructure as code via CDK; error monitoring APIs; feature flags), error reporting (Sentry), and built frameworks for unit- and integration tests", 3),
            ("- Designed and implemented integrations (Docusign, Salesforce, Flinx, Conquest, Canada Post, D1G1T, MX, National Bank Independant Network)", 2),
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
            ("- Scaled internal tooling to support large scale operations", 1),
            ("- Mentored junior engineers and interns", 1),
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


skill_categories: List[SkillCategory] = [
    SkillCategory(
        category="Software Architecture \& Design",
        skills=[
            SubCategory(
                subcategory="General Design",
                items=[
                    "Backend architecture design (traditional and serverless)",
                    "API Design",
                    "Automation design"
                ]
            ),
            SubCategory(
                subcategory="Database Design",
                items=[
                    "Relational (SQL) and non-relational (noSQL) database design"
                ]
            )
        ]
    ),
    SkillCategory(
        category="Cloud Platforms \& Tools",
        skills=[
            SubCategory(
                subcategory="AWS Services",
                items=[
                    "AIM", "API Gateway", "AppConfig", "Athena", "Cognito", 
                    "CodeBuild", "CodePipeline", "CloudFront", "CDK", "DocumentDb", 
                    "DynamoDb", "EC2", "ECS", "EFS", "IAM", "Glue", "Lambda", 
                    "Parameter Store", "Route 53", "RDS", "Redshift", "S3", 
                    "SSM", "SNS"
                ]
            ),
            SubCategory(
                subcategory="Containerization Tools",
                items=[
                    "Docker"
                ]
            )
        ]
    ),
    SkillCategory(
        category="Development Tools \& Practices",
        skills=[
            SubCategory(
                subcategory="Observability",
                items=[
                    "DataDog", "Grafana", "Prometheus"
                ]
            ),
            SubCategory(
                subcategory="Version Control Systems",
                items=[
                    "Git", "BitBucket", "GitHub", "GitLab"
                ]
            ),
            SubCategory(
                subcategory="Operating Systems",
                items=[
                    "Linux (Ubuntu, Amazon)"
                ]
            ),
            SubCategory(
                subcategory="Other Tools",
                items=[
                    "Segment", "Sentry"
                ]
            )
        ]
    ),
    SkillCategory(
        category="Programming Languages",
        skills=[
            SubCategory(
                subcategory="Languages",
                items=[
                    "Python", "Typescript", "JavaScript", "Bash", "Powershell", "AppleScripts"
                ]
            )
        ]
    ),
    SkillCategory(
        category="Data \& Database Management",
        skills=[
            SubCategory(
                subcategory="Database Types",
                items=[
                    "SQL", "NoSQL"
                ]
            )
        ]
    ),
    SkillCategory(
        category="Mathematics \& Computational Modeling",
        skills=[
            SubCategory(
                subcategory="Topics",
                items=[
                    "Calculus", "Cluster analyses", "Discrete Mathematics", "Partial Differential Equations (PDEs)"
                ]
            )
        ]
    )
]
