DOCUMENTS = [
    {
      "id": "doc-001",
      "entity_type": "document",
      "name": "Atlas Architecture Overview",
      "summary": "Atlas combines lexical and vector retrieval with a knowledge graph.",
      "document_type": "architecture",
      "status": "published",
      "created_at": "2026-08-12",
      "updated_at": "2026-08-12",
      "access": {
        "classification": "internal",
        "allowed_groups": [
          "Engineering",
          "Product",
          "Security"
        ]
      },
      "source_uri": "https://knowledge.meridian.example/documents/001",
      "content": "Atlas combines lexical and vector retrieval with a knowledge graph. Entities use stable identifiers shared across ingestion, indexing, and graph storage. Documents are chunked by headings; each chunk retains its parent document ID. Graph expansion is limited to two hops for the pilot to control latency and irrelevant context.",
      "chunks": [
        {
          "id": "chunk-001-001",
          "document_id": "doc-001",
          "heading": "Atlas Architecture Overview",
          "text": "Atlas combines lexical and vector retrieval with a knowledge graph. Entities use stable identifiers shared across ingestion, indexing, and graph storage. Documents are chunked by headings; each chunk retains its parent document ID. Graph expansion is limited to two hops for the pilot to control latency and irrelevant context."
        }
      ],
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-001"
        },
        {
          "type": "AUTHORED_BY",
          "target_id": "omar_patel"
        }
      ],
      "retrieval_text": "Atlas Architecture Overview. Atlas combines lexical and vector retrieval with a knowledge graph. Atlas combines lexical and vector retrieval with a knowledge graph. Entities use stable identifiers shared across ingestion, indexing, and graph storage. Documents are chunked by headings; each chunk retains its parent document ID. Graph expansion is limited to two hops for the pilot to control latency and irrelevant context. Status: published. about project Atlas Knowledge Hub (project-001). authored by Omar Patel (omar_patel)."
    },
    {
      "id": "doc-002",
      "entity_type": "document",
      "name": "Orion Ingestion Contract",
      "summary": "Every ingested item must include a source ID, owner, modification timestamp, access labels, and content checksum.",
      "document_type": "specification",
      "status": "published",
      "created_at": "2026-07-20",
      "updated_at": "2026-07-20",
      "access": {
        "classification": "internal",
        "allowed_groups": [
          "Engineering",
          "Product",
          "Security"
        ]
      },
      "source_uri": "https://knowledge.meridian.example/documents/002",
      "content": "Every ingested item must include a source ID, owner, modification timestamp, access labels, and content checksum. Orion emits a normalized document event after validation. Failed records enter a quarantine queue, while successful records update both the search index and graph.",
      "chunks": [
        {
          "id": "chunk-002-001",
          "document_id": "doc-002",
          "heading": "Orion Ingestion Contract",
          "text": "Every ingested item must include a source ID, owner, modification timestamp, access labels, and content checksum. Orion emits a normalized document event after validation. Failed records enter a quarantine queue, while successful records update both the search index and graph."
        }
      ],
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-002"
        },
        {
          "type": "AUTHORED_BY",
          "target_id": "omar_patel"
        }
      ],
      "retrieval_text": "Orion Ingestion Contract. Every ingested item must include a source ID, owner, modification timestamp, access labels, and content checksum. Every ingested item must include a source ID, owner, modification timestamp, access labels, and content checksum. Orion emits a normalized document event after validation. Failed records enter a quarantine queue, while successful records update both the search index and graph. Status: published. about project Orion Data Platform (project-002). authored by Omar Patel (omar_patel)."
    },
    {
      "id": "doc-003",
      "entity_type": "document",
      "name": "Sentinel Authorization Policy",
      "summary": "Authorization must be checked before retrieval candidates reach an answer generator.",
      "document_type": "policy",
      "status": "published",
      "created_at": "2026-08-05",
      "updated_at": "2026-08-05",
      "access": {
        "classification": "internal",
        "allowed_groups": [
          "Engineering",
          "Security"
        ]
      },
      "source_uri": "https://knowledge.meridian.example/documents/003",
      "content": "Authorization must be checked before retrieval candidates reach an answer generator. The same access labels apply to vector search results and graph-expanded documents. Unknown or missing access labels default to deny. Security owns the policy and reviews exceptions monthly.",
      "chunks": [
        {
          "id": "chunk-003-001",
          "document_id": "doc-003",
          "heading": "Sentinel Authorization Policy",
          "text": "Authorization must be checked before retrieval candidates reach an answer generator. The same access labels apply to vector search results and graph-expanded documents. Unknown or missing access labels default to deny. Security owns the policy and reviews exceptions monthly."
        }
      ],
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-003"
        },
        {
          "type": "AUTHORED_BY",
          "target_id": "noah_williams"
        }
      ],
      "retrieval_text": "Sentinel Authorization Policy. Authorization must be checked before retrieval candidates reach an answer generator. Authorization must be checked before retrieval candidates reach an answer generator. The same access labels apply to vector search results and graph-expanded documents. Unknown or missing access labels default to deny. Security owns the policy and reviews exceptions monthly. Status: published. about project Sentinel Access Control (project-003). authored by Noah Williams (noah_williams)."
    },
    {
      "id": "doc-004",
      "entity_type": "document",
      "name": "Beacon Benchmark Design",
      "summary": "The benchmark contains 200 planned queries: 100 factual lookups, 60 multi-hop questions, and 40 access-sensitive questions.",
      "document_type": "evaluation_plan",
      "status": "published",
      "created_at": "2026-09-10",
      "updated_at": "2026-09-10",
      "access": {
        "classification": "internal",
        "allowed_groups": [
          "Engineering",
          "Product",
          "Security"
        ]
      },
      "source_uri": "https://knowledge.meridian.example/documents/004",
      "content": "The benchmark contains 200 planned queries: 100 factual lookups, 60 multi-hop questions, and 40 access-sensitive questions. Report retrieval recall, citation precision, answer faithfulness, and unauthorized disclosure rate separately. Product and Security review the benchmark before release.",
      "chunks": [
        {
          "id": "chunk-004-001",
          "document_id": "doc-004",
          "heading": "Beacon Benchmark Design",
          "text": "The benchmark contains 200 planned queries: 100 factual lookups, 60 multi-hop questions, and 40 access-sensitive questions. Report retrieval recall, citation precision, answer faithfulness, and unauthorized disclosure rate separately. Product and Security review the benchmark before release."
        }
      ],
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-004"
        },
        {
          "type": "AUTHORED_BY",
          "target_id": "elena_rossi"
        }
      ],
      "retrieval_text": "Beacon Benchmark Design. The benchmark contains 200 planned queries: 100 factual lookups, 60 multi-hop questions, and 40 access-sensitive questions. The benchmark contains 200 planned queries: 100 factual lookups, 60 multi-hop questions, and 40 access-sensitive questions. Report retrieval recall, citation precision, answer faithfulness, and unauthorized disclosure rate separately. Product and Security review the benchmark before release. Status: published. about project Beacon Evaluation (project-004). authored by Elena Rossi (elena_rossi)."
    },
    {
      "id": "doc-005",
      "entity_type": "document",
      "name": "Compass Onboarding Retrospective",
      "summary": "The onboarding pilot reduced median time to first contribution from 14 to 9 working days across 18 new hires.",
      "document_type": "retrospective",
      "status": "published",
      "created_at": "2026-09-30",
      "updated_at": "2026-09-30",
      "access": {
        "classification": "internal",
        "allowed_groups": [
          "Engineering",
          "Product",
          "Security"
        ]
      },
      "source_uri": "https://knowledge.meridian.example/documents/005",
      "content": "The onboarding pilot reduced median time to first contribution from 14 to 9 working days across 18 new hires. Participants valued role-specific learning paths and named document owners. Stale links remained the most frequent complaint; monthly ownership reviews were recommended.",
      "chunks": [
        {
          "id": "chunk-005-001",
          "document_id": "doc-005",
          "heading": "Compass Onboarding Retrospective",
          "text": "The onboarding pilot reduced median time to first contribution from 14 to 9 working days across 18 new hires. Participants valued role-specific learning paths and named document owners. Stale links remained the most frequent complaint; monthly ownership reviews were recommended."
        }
      ],
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-005"
        },
        {
          "type": "AUTHORED_BY",
          "target_id": "sofia_alvarez"
        }
      ],
      "retrieval_text": "Compass Onboarding Retrospective. The onboarding pilot reduced median time to first contribution from 14 to 9 working days across 18 new hires. The onboarding pilot reduced median time to first contribution from 14 to 9 working days across 18 new hires. Participants valued role-specific learning paths and named document owners. Stale links remained the most frequent complaint; monthly ownership reviews were recommended. Status: published. about project Compass Onboarding (project-005). authored by Sofia Alvarez (sofia_alvarez)."
    },
    {
      "id": "doc-006",
      "entity_type": "document",
      "name": "Harbor Reliability Proposal",
      "summary": "Harbor proposes a 99.9% monthly availability SLO for the knowledge API.",
      "document_type": "proposal",
      "status": "published",
      "created_at": "2026-10-10",
      "updated_at": "2026-10-10",
      "access": {
        "classification": "internal",
        "allowed_groups": [
          "Engineering",
          "Product",
          "Security"
        ]
      },
      "source_uri": "https://knowledge.meridian.example/documents/006",
      "content": "Harbor proposes a 99.9% monthly availability SLO for the knowledge API. Initial scope includes dependency health checks, ingestion freshness alerts, and recovery exercises. Work is planned for November and the SLO has not yet been approved.",
      "chunks": [
        {
          "id": "chunk-006-001",
          "document_id": "doc-006",
          "heading": "Harbor Reliability Proposal",
          "text": "Harbor proposes a 99.9% monthly availability SLO for the knowledge API. Initial scope includes dependency health checks, ingestion freshness alerts, and recovery exercises. Work is planned for November and the SLO has not yet been approved."
        }
      ],
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-006"
        },
        {
          "type": "AUTHORED_BY",
          "target_id": "james_okafor"
        }
      ],
      "retrieval_text": "Harbor Reliability Proposal. Harbor proposes a 99.9% monthly availability SLO for the knowledge API. Harbor proposes a 99.9% monthly availability SLO for the knowledge API. Initial scope includes dependency health checks, ingestion freshness alerts, and recovery exercises. Work is planned for November and the SLO has not yet been approved. Status: published. about project Harbor Reliability (project-006). authored by James Okafor (james_okafor)."
    },
    {
      "id": "doc-007",
      "entity_type": "document",
      "name": "Atlas Retrieval Pilot Results",
      "summary": "On an initial 60-query development set, hybrid retrieval achieved 0.82 recall at 10 compared with 0.71 for vector-only retrieval.",
      "document_type": "experiment_report",
      "status": "published",
      "created_at": "2026-09-25",
      "updated_at": "2026-09-25",
      "access": {
        "classification": "internal",
        "allowed_groups": [
          "Engineering",
          "Product",
          "Security"
        ]
      },
      "source_uri": "https://knowledge.meridian.example/documents/007",
      "content": "On an initial 60-query development set, hybrid retrieval achieved 0.82 recall at 10 compared with 0.71 for vector-only retrieval. Two-hop graph expansion improved coverage of ownership and dependency questions but increased median latency by 120 milliseconds. These results are preliminary and do not represent the final Beacon benchmark.",
      "chunks": [
        {
          "id": "chunk-007-001",
          "document_id": "doc-007",
          "heading": "Atlas Retrieval Pilot Results",
          "text": "On an initial 60-query development set, hybrid retrieval achieved 0.82 recall at 10 compared with 0.71 for vector-only retrieval. Two-hop graph expansion improved coverage of ownership and dependency questions but increased median latency by 120 milliseconds. These results are preliminary and do not represent the final Beacon benchmark."
        }
      ],
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-001"
        },
        {
          "type": "AUTHORED_BY",
          "target_id": "elena_rossi"
        }
      ],
      "retrieval_text": "Atlas Retrieval Pilot Results. On an initial 60-query development set, hybrid retrieval achieved 0.82 recall at 10 compared with 0.71 for vector-only retrieval. On an initial 60-query development set, hybrid retrieval achieved 0.82 recall at 10 compared with 0.71 for vector-only retrieval. Two-hop graph expansion improved coverage of ownership and dependency questions but increased median latency by 120 milliseconds. These results are preliminary and do not represent the final Beacon benchmark. Status: published. about project Atlas Knowledge Hub (project-001). authored by Elena Rossi (elena_rossi)."
    },
    {
      "id": "doc-008",
      "entity_type": "document",
      "name": "Entity Identity and Merge Rules",
      "summary": "Use immutable IDs for people, projects, skills, documents, and decisions.",
      "document_type": "specification",
      "status": "published",
      "created_at": "2026-08-18",
      "updated_at": "2026-08-18",
      "access": {
        "classification": "internal",
        "allowed_groups": [
          "Engineering",
          "Product",
          "Security"
        ]
      },
      "source_uri": "https://knowledge.meridian.example/documents/008",
      "content": "Use immutable IDs for people, projects, skills, documents, and decisions. Match people using verified source identifiers rather than display names. Suspected duplicate entities enter manual review. Merges retain old IDs as aliases and preserve relationship provenance.",
      "chunks": [
        {
          "id": "chunk-008-001",
          "document_id": "doc-008",
          "heading": "Entity Identity and Merge Rules",
          "text": "Use immutable IDs for people, projects, skills, documents, and decisions. Match people using verified source identifiers rather than display names. Suspected duplicate entities enter manual review. Merges retain old IDs as aliases and preserve relationship provenance."
        }
      ],
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-002"
        },
        {
          "type": "AUTHORED_BY",
          "target_id": "omar_patel"
        }
      ],
      "retrieval_text": "Entity Identity and Merge Rules. Use immutable IDs for people, projects, skills, documents, and decisions. Use immutable IDs for people, projects, skills, documents, and decisions. Match people using verified source identifiers rather than display names. Suspected duplicate entities enter manual review. Merges retain old IDs as aliases and preserve relationship provenance. Status: published. about project Orion Data Platform (project-002). authored by Omar Patel (omar_patel)."
    },
    {
      "id": "doc-009",
      "entity_type": "document",
      "name": "Atlas Product Requirements",
      "summary": "Employees need to find project owners, understand technical decisions, and discover relevant expertise.",
      "document_type": "requirements",
      "status": "published",
      "created_at": "2026-06-15",
      "updated_at": "2026-06-15",
      "access": {
        "classification": "internal",
        "allowed_groups": [
          "Engineering",
          "Product",
          "Security"
        ]
      },
      "source_uri": "https://knowledge.meridian.example/documents/009",
      "content": "Employees need to find project owners, understand technical decisions, and discover relevant expertise. Answers must cite supporting documents and display freshness. The pilot serves Engineering and Product. Public web search and automated policy changes are outside the pilot scope.",
      "chunks": [
        {
          "id": "chunk-009-001",
          "document_id": "doc-009",
          "heading": "Atlas Product Requirements",
          "text": "Employees need to find project owners, understand technical decisions, and discover relevant expertise. Answers must cite supporting documents and display freshness. The pilot serves Engineering and Product. Public web search and automated policy changes are outside the pilot scope."
        }
      ],
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-001"
        },
        {
          "type": "AUTHORED_BY",
          "target_id": "priya_shah"
        }
      ],
      "retrieval_text": "Atlas Product Requirements. Employees need to find project owners, understand technical decisions, and discover relevant expertise. Employees need to find project owners, understand technical decisions, and discover relevant expertise. Answers must cite supporting documents and display freshness. The pilot serves Engineering and Product. Public web search and automated policy changes are outside the pilot scope. Status: published. about project Atlas Knowledge Hub (project-001). authored by Priya Shah (priya_shah)."
    },
    {
      "id": "doc-010",
      "entity_type": "document",
      "name": "Sentinel Threat Model",
      "summary": "Threat scenarios include unauthorized document retrieval, sensitive relationship leakage, and prompt injection inside source documents.",
      "document_type": "threat_model",
      "status": "published",
      "created_at": "2026-09-03",
      "updated_at": "2026-09-03",
      "access": {
        "classification": "internal",
        "allowed_groups": [
          "Engineering",
          "Security"
        ]
      },
      "source_uri": "https://knowledge.meridian.example/documents/010",
      "content": "Threat scenarios include unauthorized document retrieval, sensitive relationship leakage, and prompt injection inside source documents. Treat retrieved content as data. Apply authorization to every graph expansion and audit denied lookups without logging sensitive document content.",
      "chunks": [
        {
          "id": "chunk-010-001",
          "document_id": "doc-010",
          "heading": "Sentinel Threat Model",
          "text": "Threat scenarios include unauthorized document retrieval, sensitive relationship leakage, and prompt injection inside source documents. Treat retrieved content as data. Apply authorization to every graph expansion and audit denied lookups without logging sensitive document content."
        }
      ],
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-003"
        },
        {
          "type": "AUTHORED_BY",
          "target_id": "noah_williams"
        }
      ],
      "retrieval_text": "Sentinel Threat Model. Threat scenarios include unauthorized document retrieval, sensitive relationship leakage, and prompt injection inside source documents. Threat scenarios include unauthorized document retrieval, sensitive relationship leakage, and prompt injection inside source documents. Treat retrieved content as data. Apply authorization to every graph expansion and audit denied lookups without logging sensitive document content. Status: published. about project Sentinel Access Control (project-003). authored by Noah Williams (noah_williams)."
    },
    {
      "id": "doc-011",
      "entity_type": "document",
      "name": "Knowledge Content Ownership Guide",
      "summary": "Each knowledge document needs a named owner and review date.",
      "document_type": "guide",
      "status": "published",
      "created_at": "2026-08-22",
      "updated_at": "2026-08-22",
      "access": {
        "classification": "internal",
        "allowed_groups": [
          "Engineering",
          "Product",
          "Security"
        ]
      },
      "source_uri": "https://knowledge.meridian.example/documents/011",
      "content": "Each knowledge document needs a named owner and review date. Project owners review architecture and decision records quarterly; policy owners review access rules monthly. Archived content stays available for historical questions with an explicit archived label.",
      "chunks": [
        {
          "id": "chunk-011-001",
          "document_id": "doc-011",
          "heading": "Knowledge Content Ownership Guide",
          "text": "Each knowledge document needs a named owner and review date. Project owners review architecture and decision records quarterly; policy owners review access rules monthly. Archived content stays available for historical questions with an explicit archived label."
        }
      ],
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-005"
        },
        {
          "type": "AUTHORED_BY",
          "target_id": "sofia_alvarez"
        }
      ],
      "retrieval_text": "Knowledge Content Ownership Guide. Each knowledge document needs a named owner and review date. Each knowledge document needs a named owner and review date. Project owners review architecture and decision records quarterly; policy owners review access rules monthly. Archived content stays available for historical questions with an explicit archived label. Status: published. about project Compass Onboarding (project-005). authored by Sofia Alvarez (sofia_alvarez)."
    },
    {
      "id": "doc-012",
      "entity_type": "document",
      "name": "Beacon Review Notes",
      "summary": "Product requested explicit multi-hop coverage for questions linking skills, project membership, and decisions.",
      "document_type": "meeting_notes",
      "status": "published",
      "created_at": "2026-10-08",
      "updated_at": "2026-10-08",
      "access": {
        "classification": "internal",
        "allowed_groups": [
          "Engineering",
          "Product",
          "Security"
        ]
      },
      "source_uri": "https://knowledge.meridian.example/documents/012",
      "content": "Product requested explicit multi-hop coverage for questions linking skills, project membership, and decisions. Security requested separate reporting for access-sensitive cases. The team agreed that Atlas launch approval requires benchmark review and a clean authorization test run.",
      "chunks": [
        {
          "id": "chunk-012-001",
          "document_id": "doc-012",
          "heading": "Beacon Review Notes",
          "text": "Product requested explicit multi-hop coverage for questions linking skills, project membership, and decisions. Security requested separate reporting for access-sensitive cases. The team agreed that Atlas launch approval requires benchmark review and a clean authorization test run."
        }
      ],
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-004"
        },
        {
          "type": "AUTHORED_BY",
          "target_id": "priya_shah"
        }
      ],
      "retrieval_text": "Beacon Review Notes. Product requested explicit multi-hop coverage for questions linking skills, project membership, and decisions. Product requested explicit multi-hop coverage for questions linking skills, project membership, and decisions. Security requested separate reporting for access-sensitive cases. The team agreed that Atlas launch approval requires benchmark review and a clean authorization test run. Status: published. about project Beacon Evaluation (project-004). authored by Priya Shah (priya_shah)."
    }
  ]
