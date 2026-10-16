DECISIONS = [
    {
      "id": "decision-001",
      "entity_type": "decision",
      "name": "Use hybrid retrieval for Atlas",
      "summary": "Combine lexical and vector retrieval for the pilot.",
      "status": "accepted",
      "recorded_at": "2026-09-28",
      "rationale": "The development-set experiment showed improved recall over vector-only retrieval.",
      "alternatives_considered": [
        "Vector-only retrieval",
        "Lexical-only retrieval"
      ],
      "consequences": "Adds ranking configuration and requires evaluation on the final benchmark.",
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-001"
        },
        {
          "type": "PROPOSED_BY",
          "target_id": "elena_rossi"
        },
        {
          "type": "SUPPORTED_BY",
          "target_id": "doc-001"
        },
        {
          "type": "SUPPORTED_BY",
          "target_id": "doc-007"
        },
        {
          "type": "APPROVED_BY",
          "target_id": "maya_chen"
        }
      ],
      "retrieval_text": "Use hybrid retrieval for Atlas. Combine lexical and vector retrieval for the pilot. The development-set experiment showed improved recall over vector-only retrieval. Adds ranking configuration and requires evaluation on the final benchmark. Status: accepted. about project Atlas Knowledge Hub (project-001). proposed by Elena Rossi (elena_rossi). supported by Atlas Architecture Overview (doc-001). supported by Atlas Retrieval Pilot Results (doc-007). approved by Maya Chen (maya_chen)."
    },
    {
      "id": "decision-002",
      "entity_type": "decision",
      "name": "Enforce authorization before generation",
      "summary": "Filter retrieval and graph expansion using document access labels.",
      "status": "accepted",
      "recorded_at": "2026-08-08",
      "rationale": "Consistent early filtering reduces disclosure risk across retrieval paths.",
      "alternatives_considered": [
        "Filter only the final answer"
      ],
      "consequences": "Adds authorization checks to each retrieval path.",
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-003"
        },
        {
          "type": "PROPOSED_BY",
          "target_id": "noah_williams"
        },
        {
          "type": "SUPPORTED_BY",
          "target_id": "doc-003"
        },
        {
          "type": "SUPPORTED_BY",
          "target_id": "doc-010"
        },
        {
          "type": "APPROVED_BY",
          "target_id": "maya_chen"
        }
      ],
      "retrieval_text": "Enforce authorization before generation. Filter retrieval and graph expansion using document access labels. Consistent early filtering reduces disclosure risk across retrieval paths. Adds authorization checks to each retrieval path. Status: accepted. about project Sentinel Access Control (project-003). proposed by Noah Williams (noah_williams). supported by Sentinel Authorization Policy (doc-003). supported by Sentinel Threat Model (doc-010). approved by Maya Chen (maya_chen)."
    },
    {
      "id": "decision-003",
      "entity_type": "decision",
      "name": "Use immutable entity identifiers",
      "summary": "Assign stable global IDs and retain aliases after merges.",
      "status": "accepted",
      "recorded_at": "2026-08-20",
      "rationale": "Names change and are not reliable join keys.",
      "alternatives_considered": [
        "Use display names as keys"
      ],
      "consequences": "Requires identity resolution and merge provenance.",
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-002"
        },
        {
          "type": "PROPOSED_BY",
          "target_id": "omar_patel"
        },
        {
          "type": "SUPPORTED_BY",
          "target_id": "doc-002"
        },
        {
          "type": "SUPPORTED_BY",
          "target_id": "doc-008"
        },
        {
          "type": "APPROVED_BY",
          "target_id": "maya_chen"
        }
      ],
      "retrieval_text": "Use immutable entity identifiers. Assign stable global IDs and retain aliases after merges. Names change and are not reliable join keys. Requires identity resolution and merge provenance. Status: accepted. about project Orion Data Platform (project-002). proposed by Omar Patel (omar_patel). supported by Orion Ingestion Contract (doc-002). supported by Entity Identity and Merge Rules (doc-008). approved by Maya Chen (maya_chen)."
    },
    {
      "id": "decision-004",
      "entity_type": "decision",
      "name": "Limit graph expansion to two hops",
      "summary": "Cap pilot graph traversal at two hops.",
      "status": "accepted",
      "recorded_at": "2026-09-29",
      "rationale": "Pilot results showed useful coverage with measurable latency overhead.",
      "alternatives_considered": [
        "Unlimited traversal",
        "No graph expansion"
      ],
      "consequences": "Some longer dependency chains will require follow-up queries.",
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-001"
        },
        {
          "type": "PROPOSED_BY",
          "target_id": "omar_patel"
        },
        {
          "type": "SUPPORTED_BY",
          "target_id": "doc-001"
        },
        {
          "type": "SUPPORTED_BY",
          "target_id": "doc-007"
        },
        {
          "type": "APPROVED_BY",
          "target_id": "maya_chen"
        }
      ],
      "retrieval_text": "Limit graph expansion to two hops. Cap pilot graph traversal at two hops. Pilot results showed useful coverage with measurable latency overhead. Some longer dependency chains will require follow-up queries. Status: accepted. about project Atlas Knowledge Hub (project-001). proposed by Omar Patel (omar_patel). supported by Atlas Architecture Overview (doc-001). supported by Atlas Retrieval Pilot Results (doc-007). approved by Maya Chen (maya_chen)."
    },
    {
      "id": "decision-005",
      "entity_type": "decision",
      "name": "Adopt a 99.9% availability SLO",
      "summary": "Target 99.9% monthly availability after production readiness review.",
      "status": "proposed",
      "recorded_at": "2026-10-12",
      "rationale": "The knowledge API will support daily employee workflows.",
      "alternatives_considered": [
        "99.5% availability target"
      ],
      "consequences": "Requires operational staffing and alert tuning; approval is pending.",
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-006"
        },
        {
          "type": "PROPOSED_BY",
          "target_id": "james_okafor"
        },
        {
          "type": "SUPPORTED_BY",
          "target_id": "doc-006"
        }
      ],
      "retrieval_text": "Adopt a 99.9% availability SLO. Target 99.9% monthly availability after production readiness review. The knowledge API will support daily employee workflows. Requires operational staffing and alert tuning; approval is pending. Status: proposed. about project Harbor Reliability (project-006). proposed by James Okafor (james_okafor). supported by Harbor Reliability Proposal (doc-006)."
    },
    {
      "id": "decision-006",
      "entity_type": "decision",
      "name": "Require benchmark review before launch",
      "summary": "Gate Atlas launch on Beacon review and clean authorization tests.",
      "status": "accepted",
      "recorded_at": "2026-10-09",
      "rationale": "Launch quality must include multi-hop reasoning and access-sensitive behavior.",
      "alternatives_considered": [
        "Launch based on informal user feedback"
      ],
      "consequences": "May delay launch if benchmark gaps remain.",
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-001"
        },
        {
          "type": "PROPOSED_BY",
          "target_id": "priya_shah"
        },
        {
          "type": "SUPPORTED_BY",
          "target_id": "doc-004"
        },
        {
          "type": "SUPPORTED_BY",
          "target_id": "doc-012"
        },
        {
          "type": "APPROVED_BY",
          "target_id": "maya_chen"
        }
      ],
      "retrieval_text": "Require benchmark review before launch. Gate Atlas launch on Beacon review and clean authorization tests. Launch quality must include multi-hop reasoning and access-sensitive behavior. May delay launch if benchmark gaps remain. Status: accepted. about project Atlas Knowledge Hub (project-001). proposed by Priya Shah (priya_shah). supported by Beacon Benchmark Design (doc-004). supported by Beacon Review Notes (doc-012). approved by Maya Chen (maya_chen)."
    },
    {
      "id": "decision-007",
      "entity_type": "decision",
      "name": "Retain archived knowledge with labels",
      "summary": "Keep archived documents searchable with explicit historical labels.",
      "status": "accepted",
      "recorded_at": "2026-09-30",
      "rationale": "Historical questions need context, while users need clear freshness signals.",
      "alternatives_considered": [
        "Delete all archived content"
      ],
      "consequences": "Search ranking must distinguish current and historical sources.",
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-005"
        },
        {
          "type": "PROPOSED_BY",
          "target_id": "sofia_alvarez"
        },
        {
          "type": "SUPPORTED_BY",
          "target_id": "doc-005"
        },
        {
          "type": "SUPPORTED_BY",
          "target_id": "doc-011"
        },
        {
          "type": "APPROVED_BY",
          "target_id": "maya_chen"
        }
      ],
      "retrieval_text": "Retain archived knowledge with labels. Keep archived documents searchable with explicit historical labels. Historical questions need context, while users need clear freshness signals. Search ranking must distinguish current and historical sources. Status: accepted. about project Compass Onboarding (project-005). proposed by Sofia Alvarez (sofia_alvarez). supported by Compass Onboarding Retrospective (doc-005). supported by Knowledge Content Ownership Guide (doc-011). approved by Maya Chen (maya_chen)."
    },
    {
      "id": "decision-008",
      "entity_type": "decision",
      "name": "Replace hybrid retrieval with vector-only search",
      "summary": "Do not adopt the proposal to remove lexical retrieval.",
      "status": "rejected",
      "recorded_at": "2026-10-02",
      "rationale": "The current pilot evidence favors hybrid retrieval and exact term matching remains useful.",
      "alternatives_considered": [
        "Keep hybrid retrieval"
      ],
      "consequences": "Continue maintaining both retrieval paths.",
      "relationships": [
        {
          "type": "ABOUT_PROJECT",
          "target_id": "project-001"
        },
        {
          "type": "PROPOSED_BY",
          "target_id": "maya_chen"
        },
        {
          "type": "SUPPORTED_BY",
          "target_id": "doc-007"
        },
        {
          "type": "SUPPORTED_BY",
          "target_id": "doc-009"
        },
        {
          "type": "CONFLICTS_WITH",
          "target_id": "decision-001"
        }
      ],
      "retrieval_text": "Replace hybrid retrieval with vector-only search. Do not adopt the proposal to remove lexical retrieval. The current pilot evidence favors hybrid retrieval and exact term matching remains useful. Continue maintaining both retrieval paths. Status: rejected. about project Atlas Knowledge Hub (project-001). proposed by Maya Chen (maya_chen). supported by Atlas Retrieval Pilot Results (doc-007). supported by Atlas Product Requirements (doc-009). conflicts with Use hybrid retrieval for Atlas (decision-001)."
    }
  ]