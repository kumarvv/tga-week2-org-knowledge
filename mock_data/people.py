PEOPLE = [
    {
      "id": "maya_chen",
      "entity_type": "person",
      "name": "Maya Chen",
      "summary": "Maya Chen is the Head of Engineering in Engineering at Meridian Labs.",
      "role": "Head of Engineering",
      "department": "Engineering",
      "email": "maya.chen@meridian.example",
      "location": "London",
      "skill_proficiencies": [
        {
          "skill_id": "knowledge_graphs",
          "level": "expert"
        },
        {
          "skill_id": "cloud_infrastructure",
          "level": "advanced"
        },
        {
          "skill_id": "technical_writing",
          "level": "advanced"
        }
      ],
      "relationships": [
        {
          "type": "HAS_SKILL",
          "target_id": "knowledge_graphs"
        },
        {
          "type": "HAS_SKILL",
          "target_id": "cloud_infrastructure"
        },
        {
          "type": "HAS_SKILL",
          "target_id": "technical_writing"
        }
      ],
      "retrieval_text": "Maya Chen. Maya Chen is the Head of Engineering in Engineering at Meridian Labs. Head of Engineering Engineering has skill Knowledge Graphs (knowledge_graphs). has skill Cloud Infrastructure (cloud_infrastructure). has skill Technical Writing (technical_writing)."
    },
    {
      "id": "omar_patel",
      "entity_type": "person",
      "name": "Omar Patel",
      "summary": "Omar Patel is the Staff Data Engineer in Data Platform at Meridian Labs.",
      "role": "Staff Data Engineer",
      "department": "Data Platform",
      "email": "omar.patel@meridian.example",
      "location": "New York",
      "skill_proficiencies": [
        {
          "skill_id": "python",
          "level": "expert"
        },
        {
          "skill_id": "knowledge_graphs",
          "level": "advanced"
        },
        {
          "skill_id": "data_governance",
          "level": "advanced"
        }
      ],
      "relationships": [
        {
          "type": "HAS_SKILL",
          "target_id": "python"
        },
        {
          "type": "HAS_SKILL",
          "target_id": "knowledge_graphs"
        },
        {
          "type": "HAS_SKILL",
          "target_id": "data_governance"
        },
        {
          "type": "REPORTS_TO",
          "target_id": "maya_chen"
        }
      ],
      "retrieval_text": "Omar Patel. Omar Patel is the Staff Data Engineer in Data Platform at Meridian Labs. Staff Data Engineer Data Platform has skill Python (python). has skill Knowledge Graphs (knowledge_graphs). has skill Data Governance (data_governance). reports to Maya Chen (maya_chen)."
    },
    {
      "id": "elena_rossi",
      "entity_type": "person",
      "name": "Elena Rossi",
      "summary": "Elena Rossi is the Search Scientist in Applied AI at Meridian Labs.",
      "role": "Search Scientist",
      "department": "Applied AI",
      "email": "elena.rossi@meridian.example",
      "location": "Toronto",
      "skill_proficiencies": [
        {
          "skill_id": "python",
          "level": "expert"
        },
        {
          "skill_id": "information_retrieval",
          "level": "advanced"
        },
        {
          "skill_id": "experiment_design",
          "level": "advanced"
        }
      ],
      "relationships": [
        {
          "type": "HAS_SKILL",
          "target_id": "python"
        },
        {
          "type": "HAS_SKILL",
          "target_id": "information_retrieval"
        },
        {
          "type": "HAS_SKILL",
          "target_id": "experiment_design"
        },
        {
          "type": "REPORTS_TO",
          "target_id": "maya_chen"
        }
      ],
      "retrieval_text": "Elena Rossi. Elena Rossi is the Search Scientist in Applied AI at Meridian Labs. Search Scientist Applied AI has skill Python (python). has skill Information Retrieval (information_retrieval). has skill Experiment Design (experiment_design). reports to Maya Chen (maya_chen)."
    },
    {
      "id": "noah_williams",
      "entity_type": "person",
      "name": "Noah Williams",
      "summary": "Noah Williams is the Security Lead in Security at Meridian Labs.",
      "role": "Security Lead",
      "department": "Security",
      "email": "noah.williams@meridian.example",
      "location": "Boston",
      "skill_proficiencies": [
        {
          "skill_id": "data_governance",
          "level": "expert"
        },
        {
          "skill_id": "cloud_infrastructure",
          "level": "advanced"
        },
        {
          "skill_id": "security_engineering",
          "level": "advanced"
        }
      ],
      "relationships": [
        {
          "type": "HAS_SKILL",
          "target_id": "data_governance"
        },
        {
          "type": "HAS_SKILL",
          "target_id": "cloud_infrastructure"
        },
        {
          "type": "HAS_SKILL",
          "target_id": "security_engineering"
        },
        {
          "type": "REPORTS_TO",
          "target_id": "maya_chen"
        }
      ],
      "retrieval_text": "Noah Williams. Noah Williams is the Security Lead in Security at Meridian Labs. Security Lead Security has skill Data Governance (data_governance). has skill Cloud Infrastructure (cloud_infrastructure). has skill Security Engineering (security_engineering). reports to Maya Chen (maya_chen)."
    },
    {
      "id": "priya_shah",
      "entity_type": "person",
      "name": "Priya Shah",
      "summary": "Priya Shah is the Product Manager in Product at Meridian Labs.",
      "role": "Product Manager",
      "department": "Product",
      "email": "priya.shah@meridian.example",
      "location": "London",
      "skill_proficiencies": [
        {
          "skill_id": "product_discovery",
          "level": "expert"
        },
        {
          "skill_id": "technical_writing",
          "level": "advanced"
        },
        {
          "skill_id": "experiment_design",
          "level": "advanced"
        }
      ],
      "relationships": [
        {
          "type": "HAS_SKILL",
          "target_id": "product_discovery"
        },
        {
          "type": "HAS_SKILL",
          "target_id": "technical_writing"
        },
        {
          "type": "HAS_SKILL",
          "target_id": "experiment_design"
        }
      ],
      "retrieval_text": "Priya Shah. Priya Shah is the Product Manager in Product at Meridian Labs. Product Manager Product has skill Product Discovery (product_discovery). has skill Technical Writing (technical_writing). has skill Experiment Design (experiment_design)."
    },
    {
      "id": "lucas_kim",
      "entity_type": "person",
      "name": "Lucas Kim",
      "summary": "Lucas Kim is the Senior Frontend Engineer in Engineering at Meridian Labs.",
      "role": "Senior Frontend Engineer",
      "department": "Engineering",
      "email": "lucas.kim@meridian.example",
      "location": "New York",
      "skill_proficiencies": [
        {
          "skill_id": "typescript",
          "level": "expert"
        },
        {
          "skill_id": "information_retrieval",
          "level": "advanced"
        }
      ],
      "relationships": [
        {
          "type": "HAS_SKILL",
          "target_id": "typescript"
        },
        {
          "type": "HAS_SKILL",
          "target_id": "information_retrieval"
        },
        {
          "type": "REPORTS_TO",
          "target_id": "maya_chen"
        }
      ],
      "retrieval_text": "Lucas Kim. Lucas Kim is the Senior Frontend Engineer in Engineering at Meridian Labs. Senior Frontend Engineer Engineering has skill TypeScript (typescript). has skill Information Retrieval (information_retrieval). reports to Maya Chen (maya_chen)."
    },
    {
      "id": "sofia_alvarez",
      "entity_type": "person",
      "name": "Sofia Alvarez",
      "summary": "Sofia Alvarez is the Technical Writer in Developer Experience at Meridian Labs.",
      "role": "Technical Writer",
      "department": "Developer Experience",
      "email": "sofia.alvarez@meridian.example",
      "location": "Toronto",
      "skill_proficiencies": [
        {
          "skill_id": "data_governance",
          "level": "expert"
        },
        {
          "skill_id": "technical_writing",
          "level": "advanced"
        }
      ],
      "relationships": [
        {
          "type": "HAS_SKILL",
          "target_id": "data_governance"
        },
        {
          "type": "HAS_SKILL",
          "target_id": "technical_writing"
        },
        {
          "type": "REPORTS_TO",
          "target_id": "maya_chen"
        }
      ],
      "retrieval_text": "Sofia Alvarez. Sofia Alvarez is the Technical Writer in Developer Experience at Meridian Labs. Technical Writer Developer Experience has skill Data Governance (data_governance). has skill Technical Writing (technical_writing). reports to Maya Chen (maya_chen)."
    },
    {
      "id": "james_okafor",
      "entity_type": "person",
      "name": "James Okafor",
      "summary": "James Okafor is the Site Reliability Engineer in Infrastructure at Meridian Labs.",
      "role": "Site Reliability Engineer",
      "department": "Infrastructure",
      "email": "james.okafor@meridian.example",
      "location": "Boston",
      "skill_proficiencies": [
        {
          "skill_id": "python",
          "level": "expert"
        },
        {
          "skill_id": "cloud_infrastructure",
          "level": "advanced"
        },
        {
          "skill_id": "security_engineering",
          "level": "advanced"
        }
      ],
      "relationships": [
        {
          "type": "HAS_SKILL",
          "target_id": "python"
        },
        {
          "type": "HAS_SKILL",
          "target_id": "cloud_infrastructure"
        },
        {
          "type": "HAS_SKILL",
          "target_id": "security_engineering"
        },
        {
          "type": "REPORTS_TO",
          "target_id": "maya_chen"
        }
      ],
      "retrieval_text": "James Okafor. James Okafor is the Site Reliability Engineer in Infrastructure at Meridian Labs. Site Reliability Engineer Infrastructure has skill Python (python). has skill Cloud Infrastructure (cloud_infrastructure). has skill Security Engineering (security_engineering). reports to Maya Chen (maya_chen)."
    }
  ]
