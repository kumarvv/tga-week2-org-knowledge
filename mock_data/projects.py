PROJECTS = [
    {
      "id": "project-001",
      "entity_type": "project",
      "name": "Atlas Knowledge Hub",
      "summary": "Build permission-aware organizational search with citations and graph-based context.",
      "status": "active",
      "start_date": "2026-06-01",
      "target_end_date": "2026-12-18",
      "business_unit": "Knowledge Systems",
      "success_criteria": "At least 85% citation-supported answers on the internal benchmark.",
      "relationships": [
        {
          "type": "OWNED_BY",
          "target_id": "priya_shah"
        },
        {
          "type": "HAS_MEMBER",
          "target_id": "omar_patel"
        },
        {
          "type": "HAS_MEMBER",
          "target_id": "elena_rossi"
        },
        {
          "type": "HAS_MEMBER",
          "target_id": "lucas_kim"
        },
        {
          "type": "HAS_MEMBER",
          "target_id": "sofia_alvarez"
        },
        {
          "type": "REQUIRES_SKILL",
          "target_id": "knowledge_graphs"
        },
        {
          "type": "REQUIRES_SKILL",
          "target_id": "information_retrieval"
        },
        {
          "type": "REQUIRES_SKILL",
          "target_id": "data_governance"
        },
        {
          "type": "DEPENDS_ON",
          "target_id": "project-002"
        },
        {
          "type": "DEPENDS_ON",
          "target_id": "project-003"
        },
        {
          "type": "DEPENDS_ON",
          "target_id": "project-004"
        }
      ],
      "retrieval_text": "Atlas Knowledge Hub. Build permission-aware organizational search with citations and graph-based context. Status: active. owned by Priya Shah (priya_shah). has member Omar Patel (omar_patel). has member Elena Rossi (elena_rossi). has member Lucas Kim (lucas_kim). has member Sofia Alvarez (sofia_alvarez). requires skill Knowledge Graphs (knowledge_graphs). requires skill Information Retrieval (information_retrieval). requires skill Data Governance (data_governance). depends on Orion Data Platform (project-002). depends on Sentinel Access Control (project-003). depends on Beacon Evaluation (project-004)."
    },
    {
      "id": "project-002",
      "entity_type": "project",
      "name": "Orion Data Platform",
      "summary": "Standardize ingestion, lineage, and quality checks for internal knowledge sources.",
      "status": "active",
      "start_date": "2026-03-01",
      "target_end_date": "2026-11-30",
      "business_unit": "Knowledge Systems",
      "success_criteria": "99% of scheduled ingestion jobs complete within their freshness window.",
      "relationships": [
        {
          "type": "OWNED_BY",
          "target_id": "omar_patel"
        },
        {
          "type": "HAS_MEMBER",
          "target_id": "noah_williams"
        },
        {
          "type": "HAS_MEMBER",
          "target_id": "james_okafor"
        },
        {
          "type": "REQUIRES_SKILL",
          "target_id": "python"
        },
        {
          "type": "REQUIRES_SKILL",
          "target_id": "data_governance"
        },
        {
          "type": "REQUIRES_SKILL",
          "target_id": "cloud_infrastructure"
        }
      ],
      "retrieval_text": "Orion Data Platform. Standardize ingestion, lineage, and quality checks for internal knowledge sources. Status: active. owned by Omar Patel (omar_patel). has member Noah Williams (noah_williams). has member James Okafor (james_okafor). requires skill Python (python). requires skill Data Governance (data_governance). requires skill Cloud Infrastructure (cloud_infrastructure)."
    },
    {
      "id": "project-003",
      "entity_type": "project",
      "name": "Sentinel Access Control",
      "summary": "Apply document-level authorization consistently across search and graph traversal.",
      "status": "active",
      "start_date": "2026-05-15",
      "target_end_date": "2026-11-15",
      "business_unit": "Knowledge Systems",
      "success_criteria": "Zero unauthorized results in the access-control test suite.",
      "relationships": [
        {
          "type": "OWNED_BY",
          "target_id": "noah_williams"
        },
        {
          "type": "HAS_MEMBER",
          "target_id": "omar_patel"
        },
        {
          "type": "HAS_MEMBER",
          "target_id": "lucas_kim"
        },
        {
          "type": "HAS_MEMBER",
          "target_id": "james_okafor"
        },
        {
          "type": "REQUIRES_SKILL",
          "target_id": "data_governance"
        },
        {
          "type": "REQUIRES_SKILL",
          "target_id": "security_engineering"
        }
      ],
      "retrieval_text": "Sentinel Access Control. Apply document-level authorization consistently across search and graph traversal. Status: active. owned by Noah Williams (noah_williams). has member Omar Patel (omar_patel). has member Lucas Kim (lucas_kim). has member James Okafor (james_okafor). requires skill Data Governance (data_governance). requires skill Security Engineering (security_engineering)."
    },
    {
      "id": "project-004",
      "entity_type": "project",
      "name": "Beacon Evaluation",
      "summary": "Measure grounded answers, retrieval coverage, and multi-hop reasoning quality.",
      "status": "active",
      "start_date": "2026-07-01",
      "target_end_date": "2026-12-01",
      "business_unit": "Knowledge Systems",
      "success_criteria": "A reviewed benchmark of 200 queries with single-hop and multi-hop labels.",
      "relationships": [
        {
          "type": "OWNED_BY",
          "target_id": "elena_rossi"
        },
        {
          "type": "HAS_MEMBER",
          "target_id": "priya_shah"
        },
        {
          "type": "HAS_MEMBER",
          "target_id": "sofia_alvarez"
        },
        {
          "type": "REQUIRES_SKILL",
          "target_id": "information_retrieval"
        },
        {
          "type": "REQUIRES_SKILL",
          "target_id": "experiment_design"
        },
        {
          "type": "DEPENDS_ON",
          "target_id": "project-002"
        }
      ],
      "retrieval_text": "Beacon Evaluation. Measure grounded answers, retrieval coverage, and multi-hop reasoning quality. Status: active. owned by Elena Rossi (elena_rossi). has member Priya Shah (priya_shah). has member Sofia Alvarez (sofia_alvarez). requires skill Information Retrieval (information_retrieval). requires skill Experiment Design (experiment_design). depends on Orion Data Platform (project-002)."
    },
    {
      "id": "project-005",
      "entity_type": "project",
      "name": "Compass Onboarding",
      "summary": "Reduce new employee onboarding friction using curated learning paths.",
      "status": "completed",
      "start_date": "2026-02-01",
      "target_end_date": "2026-09-30",
      "business_unit": "Knowledge Systems",
      "success_criteria": "Median time to first successful contribution below 10 working days.",
      "relationships": [
        {
          "type": "OWNED_BY",
          "target_id": "sofia_alvarez"
        },
        {
          "type": "HAS_MEMBER",
          "target_id": "priya_shah"
        },
        {
          "type": "HAS_MEMBER",
          "target_id": "lucas_kim"
        },
        {
          "type": "REQUIRES_SKILL",
          "target_id": "product_discovery"
        },
        {
          "type": "REQUIRES_SKILL",
          "target_id": "technical_writing"
        }
      ],
      "retrieval_text": "Compass Onboarding. Reduce new employee onboarding friction using curated learning paths. Status: completed. owned by Sofia Alvarez (sofia_alvarez). has member Priya Shah (priya_shah). has member Lucas Kim (lucas_kim). requires skill Product Discovery (product_discovery). requires skill Technical Writing (technical_writing)."
    },
    {
      "id": "project-006",
      "entity_type": "project",
      "name": "Harbor Reliability",
      "summary": "Prepare knowledge services for production with SLOs and recovery runbooks.",
      "status": "planned",
      "start_date": "2026-11-01",
      "target_end_date": "2027-01-29",
      "business_unit": "Knowledge Systems",
      "success_criteria": "Approved 99.9% availability target and a tested recovery procedure.",
      "relationships": [
        {
          "type": "OWNED_BY",
          "target_id": "james_okafor"
        },
        {
          "type": "HAS_MEMBER",
          "target_id": "maya_chen"
        },
        {
          "type": "HAS_MEMBER",
          "target_id": "noah_williams"
        },
        {
          "type": "REQUIRES_SKILL",
          "target_id": "cloud_infrastructure"
        },
        {
          "type": "REQUIRES_SKILL",
          "target_id": "security_engineering"
        },
        {
          "type": "DEPENDS_ON",
          "target_id": "project-001"
        },
        {
          "type": "DEPENDS_ON",
          "target_id": "project-003"
        }
      ],
      "retrieval_text": "Harbor Reliability. Prepare knowledge services for production with SLOs and recovery runbooks. Status: planned. owned by James Okafor (james_okafor). has member Maya Chen (maya_chen). has member Noah Williams (noah_williams). requires skill Cloud Infrastructure (cloud_infrastructure). requires skill Security Engineering (security_engineering). depends on Atlas Knowledge Hub (project-001). depends on Sentinel Access Control (project-003)."
    }
  ]

