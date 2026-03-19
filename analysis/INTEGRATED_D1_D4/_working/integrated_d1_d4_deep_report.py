from __future__ import annotations

from collections import Counter
import re
from typing import Any

CASE_LABELS = {
    "CASE_D1": "Childhood",
    "CASE_D2": "Youth",
    "CASE_D3": "Adults",
    "CASE_D4": "Elderly",
}

QUESTION_ORDER = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7"]
QUESTION_PART = {
    "Q1": "## Part One: Core Meaning & Experience",
    "Q5": "## Part Two: Implementation (Challenges, Opportunities, Practical Suggestions)",
}
THEME_LABELS = {
    "IT1": "multidimensional balance and moral grounding",
    "IT2": "relational ecology across the life course",
    "IT3": "partial and fragmented reflection in current care",
    "IT4": "institutionally embedded redesign",
}
EVIDENCE_TYPE_LABELS = {
    "verbatim_transcript": "verbatim transcript",
    "note_style_transcript_summary": "note-style transcript summary",
    "note_taker_summary": "note-taker summary",
    "participant_contribution": "participant contribution",
    "close_reading_theme_support": "close-reading support",
}

CODE_LABELS = {
    "access_delay_waiting": "Access delay and waiting-time pressure",
    "age_dignity_language": "Ageing discussed through dignity, worth, and respectful language",
    "awareness_education": "Awareness and education as implementation routes",
    "awareness_outreach": "Public outreach and awareness-building",
    "balance_multidimensional": "Multidimensional balance across the HT pillars",
    "communication_training_need": "Need for communication training and clearer interaction standards",
    "consultation_time_pressure": "Consultation time pressure and compressed encounters",
    "contentment_acceptance": "Contentment, acceptance, and inner steadiness",
    "contentment_as_core": "Contentment framed as the core of wellbeing",
    "cultural_local_adaptation": "Need for culturally grounded local adaptation",
    "digital_admin_relief": "Administrative and digital redesign as relief points",
    "dignity_autonomy": "Dignity, autonomy, and meaningful self-direction",
    "family_caregiver_ecology": "Family and caregiver ecology around older adults",
    "family_caregiving_ecology": "Family, caregiving, and role-bearing ecology",
    "family_support_ecology": "Family and support ecology around wellbeing",
    "functionality_self_management": "Functioning, self-management, and daily livability",
    "general_response": "General response material",
    "health_literacy_navigation": "Health literacy, explanation, and navigation difficulty",
    "healthcare_system_critique": "Critique of fragmented or narrow healthcare delivery",
    "healthcare_worker_wellbeing": "Healthcare worker wellbeing as part of system quality",
    "inner_peace_stability": "Inner peace, stability, and psychological steadiness",
    "institutional_example": "Concrete institutional examples or provider-dependent good practice",
    "interdisciplinary_integration": "Interdisciplinary integration and linked service work",
    "language_cultural_mismatch": "Language and cultural mismatch in care encounters",
    "mental_health_elderly": "Mental and emotional wellbeing in older age",
    "patient_provider_relationship": "Patient-provider trust and relationship quality",
    "peer_belonging_isolation": "Peer belonging, isolation, and youth social worlds",
    "pillar_emotional": "Emotional pillar emphasis",
    "pillar_physical": "Physical pillar emphasis",
    "pillar_social": "Social pillar emphasis",
    "practical_recommendation": "Practical recommendation and implementation thinking",
    "practical_suggestion": "Concrete practical suggestion for redesign",
    "professional_identity": "Professional role and identity shaping the discussion",
    "school_clinical_link": "School-clinical linkage and early support pathways",
    "service_adequacy_reflection": "Reflection on whether current services are adequate",
    "spiritual_moral_anchor": "Spiritual and moral grounding",
    "support_as_wellbeing_core": "Support and connectedness as core to wellbeing",
    "system_responsibility_orientation": "System responsibility rather than individual blame alone",
    "top_down_system_change": "Leadership and top-down system change expectations",
    "trust_questioning_barrier": "Trust barriers and difficulty questioning providers",
    "work_life_strain": "Work-life strain and role pressure",
}

QUESTION_CONTENT: dict[str, dict[str, Any]] = {
    "Q1": {
        "title": "What is wellbeing for you?",
        "arabic": "ما معنى الحياة الطيبة بالنسبة لك؟",
        "intro": "`Q1` is the conceptual opening of the whole workshop series. It is where participants first define `الحياة الطيبة` in relation to the HT framework rather than to service problems. Across D1-D4, this question establishes the five-pillar model as a lived, value-laden way of talking about the good life, not simply as an abstract framework name.",
        "cases": {
            "CASE_D1": "The Day 1 childhood case defines wellbeing through `قناعة` (contentment), `توازن` (balance), and spiritual grounding. Read through the HT framework, childhood wellbeing is not introduced as a technical child-development score; it is framed as a morally anchored good life whose spiritual, emotional, social, physical, and intellectual parts must hold together. The strongest Day 1 `Q1` material also shows how the childhood case is mediated through adult professionals, who describe the child’s good life through safety, balance, and culturally local protection rather than through sustained child voice.",
            "CASE_D2": "The Day 2 youth case keeps the balance language but adds stronger emphasis on usefulness, self-regard, identity, and social-moral positioning. Youth wellbeing is described as being satisfied with oneself, useful to self and others, and held inside a workable relational world. Read through the HT framework, the youth case weights the social and emotional pillars heavily, but it keeps them inseparable from spiritual orientation, purpose, and the capacity to keep functioning in visible public life.",
            "CASE_D3": "The Day 3 adult case shifts the emphasis from abstract peace to livable coping under pressure. Adult wellbeing is defined through contentment, relational positioning, balance, values-action alignment, and the practical ability to keep going despite stressors. Through the HT lens, adulthood is where the framework becomes strongly role-bearing: the pillars are still integrated, but they are repeatedly tested by work, caregiving, responsibility, and the need to remain outwardly functional.",
            "CASE_D4": "The Day 4 elderly case adds the strongest dignity language. Older-age wellbeing is described through peace, faith, contentment, containment, autonomy, and the refusal to reduce an older person to burden or decline. Read through the HT framework, the elderly case weights the spiritual, emotional, and social pillars in a particularly dignity-sensitive way while still insisting that physical and cognitive realities must be held inside a broader account of personhood.",
        },
        "themes": [
            ("Inner contentment and peace", "Wellbeing is repeatedly described as calm, satisfaction, acceptance, and inner steadiness across all four days.", "Primary"),
            ("Multidimensional balance", "Physical, emotional, social, spiritual, and intellectual life are treated as interdependent rather than separable.", "Primary"),
            ("Values and spiritual grounding", "Faith, moral orientation, and culturally grounded meanings stabilize how the good life is understood.", "Primary"),
            ("Relational usefulness and contribution", "Being useful, held, socially connected, or valuable to others remains part of wellbeing, especially in youth and adulthood.", "Secondary"),
            ("Dignity and social standing", "Older-age and adult discussion add the importance of personhood, respect, and non-reduction to burden.", "Secondary"),
        ],
        "cross_day": "Taken together, `Q1` shows that the life-course workshops do not begin from illness, service gaps, or narrow definitions of health. They begin from a value-laden concept of the good life. Across all four days, wellbeing means multidimensional balance, but the social and moral weighting of that balance changes by life stage: safety and spiritual steadiness in childhood, workable identity and usefulness in youth, coping under role pressure in adulthood, and dignity-preserving balance in older age.",
    },
    "Q2": {
        "title": "When we describe someone as ‘well,’ what do we mean?",
        "arabic": "كيف تعرف العافية؟",
        "intro": "`Q2` moves from the broad meaning of `الحياة الطيبة` to the more specific judgement that a person is `بعافية`. Read through the HT framework, the question asks whether the five-pillar model is visible in lived functioning and not only in abstract principle. Across the four days, it repeatedly breaks the assumption that ‘well’ means physically fine.",
        "cases": {
            "CASE_D1": "The Day 1 childhood case uses `Q2` to distinguish broad wellbeing from the more concrete condition of `عافية` or being well. Participants accept the five pillars as a useful language of integration, but they also show that the framework must be interpreted rather than mechanically applied. Childhood wellness is therefore presented as a contextual judgement about balance, not a thin checklist of symptoms or school performance alone.",
            "CASE_D2": "In Day 2, youth wellness is strongly tied to functioning: getting up, participating, remaining productive, feeling psychologically settled, and maintaining relationships. But the youth case also shows why this is not enough. Because visible functioning is part of the definition, the discussion repeatedly warns that distress may still be hidden, especially where disclosure is stigma-sensitive or socially risky.",
            "CASE_D3": "The adult case adds responsibility, role-fit, and value orientation. Adults are described as well when they can appreciate where they are, hold their responsibilities, and keep themselves together across competing demands. Through the HT lens, adult `عافية` is not only bodily stability; it is the ability to keep the pillars in working relation under conditions of burden and constraint.",
            "CASE_D4": "The elderly case pushes the question furthest by warning that calm appearance may be misleading. Older people may hide distress because they do not want to become a burden, so being well requires a wider, 360-degree inquiry into emotional, spiritual, social, bodily, and environmental conditions. Day 4 therefore makes `Q2` a dignity-sensitive interpretive task rather than a simple observation of outward stability.",
        },
        "themes": [
            ("Holistic functioning", "Wellness requires inquiry into family, work, relationships, health, and context rather than only disease status.", "Primary"),
            ("Psychological steadiness", "Peace of mind, emotional balance, and inner regulation are central to describing someone as well.", "Primary"),
            ("Hidden distress beneath appearance", "Surface calm, functionality, or compliance may conceal anxiety, depression, burnout, or non-burden behaviour.", "Secondary"),
            ("Independence and functional ability", "Especially salient in the elderly case, but present more broadly as part of meaningful participation in daily life.", "Secondary"),
            ("Role-fit and responsibility", "Adult and youth discussions link wellness to the ability to keep life functioning without taking visible appearance at face value.", "Secondary"),
        ],
        "cross_day": "`Q2` shows the strongest shared rejection of biomedical minimalism. Across childhood, youth, adulthood, and older age, being well means more than being disease-free. It means being held together psychologically, socially, spiritually, and functionally. Just as importantly, the workshops agree that outward appearance is an unreliable guide: a child may look settled, a young person may keep functioning, an adult may keep performing roles, and an older person may avoid burdening others, while distress remains hidden underneath.",
    },
    "Q3": {
        "title": "How can the five HT pillars improve your wellbeing?",
        "arabic": "كيف تسهم الركائز الخمسة في تحسين عافيتك؟",
        "intro": "`Q3` is the richest question across the four workshops. Here participants move from defining wellbeing to explaining how the HT framework works in daily life. The five pillars are not treated as separate boxes. Participants describe them as connected, mutually reinforcing, and weighted differently across the life course.",
        "cases": {
            "CASE_D1": "The Day 1 childhood case treats `Q3` as the bridge between concept and practice. Participants explain how spiritual and emotional grounding support the other pillars, then move into the ecology through which children actually experience that support: schools, clinics, families, teachers, and early-awareness structures. Through the HT lens, childhood improvement is not only personal regulation; it is relational and institutional scaffolding around the child.",
            "CASE_D2": "The youth case gives the strongest relational reading of the pillars. Participants talk about young people as living through families, peers, schools, and digital environments, and they repeatedly elevate the social pillar because youth wellbeing is rarely sustainable in isolation. Day 2 therefore shows that the pillars matter because they shape how belonging, disconnection, identity, and support are lived.",
            "CASE_D3": "The adult case brings in a tension that is especially important for the integrated report: the pillars require self-work, but they cannot be enacted through self-discipline alone. Adults speak about responsibility toward self, children, family, and wider life, but they also insist that systems cannot be ignored. Day 3 is where the HT framework most clearly resists being turned into individual blame.",
            "CASE_D4": "The elderly case argues most strongly that the pillars are weighted rather than flat. Participants do not deny that all five pillars matter, but they repeatedly show that dignity, social significance, spiritual steadiness, and continued usefulness become especially heavy in older age. Day 4 therefore uses `Q3` to challenge reductive age narratives and to insist that improvement requires a less impoverished understanding of ageing itself.",
        },
        "themes": [
            ("Interconnected pillars", "The five pillars are treated as a system in which strengthening one domain often supports the others.", "Primary"),
            ("Spiritual coping and protection", "Faith, moral orientation, and spiritual grounding are repeatedly described as stabilizing responses to stress and uncertainty.", "Primary"),
            ("Social support as resilience", "Family, peers, schools, community, and social recognition are treated as essential resilience structures.", "Primary"),
            ("System responsibility for pillar enactment", "Participants insist that people cannot simply carry the pillars alone if institutions remain unchanged.", "Secondary"),
            ("Life-stage weighting of the pillars", "Older age especially shows that the pillars are not experienced as flat or equal in practice.", "Secondary"),
        ],
        "cross_day": "Across D1-D4, `Q3` shows that the five pillars are useful precisely because participants do not treat them as a flat checklist. The pillars improve wellbeing when they operate together, when they are carried by supportive relationships and institutions, and when their weighting matches life stage. Childhood and youth stress ecology and early support, adulthood stresses the balance between self and system responsibility, and older age stresses dignity, usefulness, and socially meaningful ageing.",
    },
    "Q4": {
        "title": "Are HT pillars reflected in current healthcare services?",
        "arabic": "هل تنعكس الركائز في خدمات الرعاية الصحية حاليا؟",
        "intro": "`Q4` is the clearest turning point from ideal to service reality. Across all four days, participants do not usually say the pillars are totally absent. Instead, they describe healthcare as only partially reflecting them. Read through the HT lens, this is the first sustained test of whether the five-pillar model has actually been embedded in care delivery rather than only endorsed in principle.",
        "cases": {
            "CASE_D1": "In the childhood case, `Q4` opens the sharp gap between the earlier moral-spiritual ideal and real childhood service conditions. Participants describe fragmented encounters, weak follow-up, narrow problem-handling, and poor coordination across systems that should support children more coherently. The result is not a denial that good practice exists, but an insistence that children encounter an uneven service ecology rather than a stable whole-person pathway.",
            "CASE_D2": "The youth case adds explicit pressure language. Participants say that empathy, relational support, and broader wellbeing often fall out of care once waiting rooms, throughput pressure, and crisis-driven models dominate the encounter. Day 2 therefore frames current services as capable of isolated whole-person gestures, but still structurally tilted toward illness response over youth wellbeing and prevention.",
            "CASE_D3": "The adult case describes the pillars as partially visible but weakly integrated. Adults can receive strong physical treatment, but participants ask what happens once the encounter ends: how living, coping, explaining, and navigating are actually sustained. Delayed appointments, uneven explanation, and the difficulty of making care feel whole-person rather than episodic are central to the Day 3 reading of `Q4`.",
            "CASE_D4": "The elderly case is especially explicit that the problem is uneven institutionalization. Participants say that some providers or services do reflect the pillars, but only in an ad hoc or locally dependent way rather than as a system-wide expectation. Older-age care is therefore described as patchily holistic: there are pockets of elder-sensitive practice, but not a consistently embedded model across the wider system.",
        },
        "themes": [
            ("Biomedical dominance", "Physical care remains the strongest and most stable element of current services, while wider pillars are less consistently held.", "Primary"),
            ("Fragmentation and short encounter time", "Siloed pathways, rushed encounters, and weak follow-up limit holistic assessment and continuity.", "Primary"),
            ("Partial rather than full institutional embedding", "Good practice exists, but it often depends on particular providers, tables, or services rather than uniform standards.", "Primary"),
            ("Relational, cultural, and spiritual gaps", "Empathy, disclosure safety, cultural fit, and spiritual meaning are unevenly integrated across current care.", "Secondary"),
            ("Variation by institution and setting", "Participants repeatedly describe pockets of strength rather than a single consistent system model.", "Secondary"),
        ],
        "cross_day": "The cross-day conclusion for `Q4` is that the pillars are visible, but not yet reliably built into care. Childhood shows the problem as fragmented child-service ecology, youth as pressure and prevention failure, adulthood as uneven explanation and navigability, and older age as patchy institutionalization. The common pattern is not total absence; it is partial reflection under conditions that still over-weight physical care and under-support the whole-person frame established earlier in the workshops.",
    },
    "Q5": {
        "title": "Main challenges integrating HT pillars into healthcare — and what makes it possible or not possible?",
        "arabic": "ما التحديات الرئيسية التي تواجه الدمج؟ وما الذي يجعل الدمج ممكنًا أو غير ممكن؟",
        "intro": "`Q5` concentrates the barrier layer across the integrated corpus. The strongest cross-day pattern is that whole-person care is blocked less by abstract disagreement than by operational culture: time pressure, weak continuity, hierarchy, communication gaps, fragmented pathways, and service environments that make disclosure, explanation, and dignity harder to sustain in real time.",
        "cases": {
            "CASE_D1": "In the childhood case, the challenge layer focuses on listening, coordination, and participatory decision-making. Participants do not say that professionals lack concern; they say the surrounding structures make good listening, inclusion, and joined-up action hard to sustain. Day 1 therefore frames childhood barriers as system failures around children rather than as isolated deficits within any one practitioner.",
            "CASE_D2": "The youth case sharpens the trust and disclosure problem. Participants describe privacy concerns, stigma, and the tendency for distress to be expressed through bodily complaint when direct disclosure feels unsafe. The challenge in Day 2 is not only time pressure; it is the difficulty of building care encounters where young people can speak safely enough for whole-person wellbeing to become visible.",
            "CASE_D3": "The adult case highlights rights awareness, the difficulty of questioning providers, hierarchy-sensitive communication, and the failure to explain complex care in ways adults can actually use. Day 3 therefore treats integration barriers as both structural and relational: adults need navigable systems, but they also need encounters in which asking questions and understanding options do not feel like challenges to authority.",
            "CASE_D4": "The elderly case combines time scarcity, staffing pressure, language mismatch, and the translational difficulty of turning dignity, inclusion, and social recognition into repeatable care practice. Day 4’s barrier layer is especially useful because it shows that even when providers endorse the values, they still struggle to operationalize them under pressured, unequal conditions.",
        },
        "themes": [
            ("Time pressure and encounter compression", "Short appointments and overloaded care environments reduce the space for listening, exploration, explanation, and relational safety.", "Primary"),
            ("Fragmented and siloed pathways", "Patients and families move across services without stable integration, continuity, or shared care logic.", "Primary"),
            ("Hierarchy, translation, and communication barriers", "Patients may not receive clear explanation, may hesitate to question clinicians, or may struggle across language and cultural mismatches.", "Primary"),
            ("Stigma, trust, and disclosure difficulty", "Especially visible in youth and adulthood, but relevant across the life course wherever distress is hidden or socially costly to reveal.", "Secondary"),
            ("Workforce and implementation strain", "Even well-intentioned providers may not be supported enough to consistently deliver the pillar-based model they endorse.", "Secondary"),
        ],
        "cross_day": "The integrated reading of `Q5` is that the main barriers are systemic and operational before they are ideological. Participants across all life stages already understand the value of whole-person care. What blocks it is the way services are currently organized: compressed time, fragmented pathways, uneven explanation, weak relational safety, and limited institutional support for carrying the wider pillars into real care delivery. What makes integration more possible is therefore not motivational rhetoric alone, but redesign, coordination, communicative safety, and culturally grounded implementation.",
    },
    "Q6": {
        "title": "What opportunities exist now to enhance integration?",
        "arabic": "ما الفرص المتاحة حاليا لتعزيز الدمج؟",
        "intro": "`Q6` is where the workshops begin to identify openings already present in the current environment. The integrated evidence is smaller and more uneven than `Q3-Q5`, but it is analytically important because participants are not speaking only in abstract aspirations. They can point to concrete entry points that already exist and could be strengthened.",
        "cases": {
            "CASE_D1": "The childhood case identifies schools as the strongest existing opportunity structure. Participants repeatedly describe school-based awareness and early education as the most realistic route for reaching children before needs deepen. Day 1 also suggests that wider community awareness and workforce support matter, but the material for `Q6` is thinner than for earlier questions, so the clearest opportunity remains the school setting itself.",
            "CASE_D2": "The youth case makes the opportunity layer highly practical. Participants point to school nurses, parent education, and earlier assessment structures as existing but underused resources. Day 2 therefore treats opportunity not as a blank future state but as latent infrastructure: settings and roles already exist, but they need stronger training, clearer purpose, and a more youth-sensitive design.",
            "CASE_D3": "The adult case identifies accessible counseling and awareness structures as the clearest current openings. Free counseling provision, stronger public campaigns, and cross-sector linkage appear as viable routes that already exist in partial form. The material for this question is not equally detailed across all sources, but the opportunity pattern is still clear.",
            "CASE_D4": "The elderly case combines service accessibility with public preparation. Participants identify home care, awareness campaigns, and technology-enabled support as real opportunity structures, but they insist these tools must be introduced carefully and without reducing older people to passive recipients. Day 4 therefore treats opportunity as something that can extend access and inclusion, but only if it remains elder-sensitive and appropriately timed.",
        },
        "themes": [
            ("School, family, and community partnerships", "Existing educational and community settings can carry earlier awareness, prevention, and support across childhood and youth.", "Primary"),
            ("Prevention and early awareness", "Participants repeatedly identify earlier, proactive framing as more effective than waiting for crisis or late presentation.", "Primary"),
            ("Accessible support entry points", "Free counseling, home care, frontline roles, and practical access routes are already present in partial form and can be strengthened.", "Primary"),
            ("Culturally meaningful framing", "Opportunities become stronger when wellbeing language is locally understandable and socially acceptable.", "Secondary"),
            ("Technology and outreach with caution", "Digital tools and home-linked services can extend care, but only when introduced with attention to fit, timing, and dignity.", "Secondary"),
        ],
        "cross_day": "The cross-day conclusion for `Q6` is that opportunity already exists, but it is scattered rather than fully integrated. Childhood and youth show the strength of school and family-linked entry points. Adulthood shows that free access points and public campaigns can already carry wellbeing work. Older age shows that home care, awareness, and careful technology use can widen reach. The consistent lesson is that opportunity is real, but it becomes transformative only when institutions strengthen and coordinate what is already available.",
    },
    "Q7": {
        "title": "What practical suggestions do you have for integrating HT pillars to improve healthcare services?",
        "arabic": "اقتراحات عملية لطرق الدمج؟",
        "intro": "`Q7` is the most redesign-oriented part of the report. The material is smaller and less even than in earlier questions, but the practical message is clear. Participants are not asking only for kinder attitudes. They are asking for change in pathways, communication, training, dignity, quality standards, and day-to-day institutional practice.",
        "cases": {
            "CASE_D1": "The childhood case has the thinnest direct quotation material in `Q7`. Even so, the practical message is clear: school-based awareness, workforce training, community wellness centers, parenting and family support, digital coordination, culturally adapted intervention frameworks, and extracurricular wellbeing activity.",
            "CASE_D2": "The youth case turns practical suggestion into communication and trust design. Participants call for social-media awareness, safer private routes to support, and clearer youth-facing signals that school and healthcare services can be trusted without judgment. Day 2 therefore keeps the practical layer strongly linked to disclosure safety and institutional confidence-building rather than generic awareness alone.",
            "CASE_D3": "The adult case moves most directly into system redesign. Participants focus on the time problem, integration of the five pillars into actual service organization, workforce training, and licensing-linked professional development. Even where the strongest late Day 3 lines are attribution-cautious, the practical direction is unmistakable: adult-care redesign requires institutions to carry the framework, not merely individual practitioners improvising it.",
            "CASE_D4": "The elderly case contains the strongest and broadest practical redesign logic. Participants propose communication training, elderly-specific clubs or social-health spaces, stronger institutional culture around the pillars, clearer rights and responsibilities, and licensing-linked training expectations. Day 4 therefore makes the practical layer highly concrete: redesign should be visible in physical access, social inclusion, professional development, and organization-wide norms.",
        },
        "themes": [
            ("Institutional redesign rather than ad hoc goodwill", "The practical layer converges on durable redesign rather than isolated interpersonal effort.", "Primary"),
            ("Communication, dignity, and trust", "Communication quality, respectful interaction, and disclosure safety are treated as core redesign issues.", "Primary"),
            ("Training, licensing, and workforce development", "Participants repeatedly link whole-person care to staff training, expectations, and professional development systems.", "Primary"),
            ("Prevention and community linkage", "Schools, families, community spaces, and outreach structures remain key implementation routes.", "Secondary"),
            ("Culturally grounded HT implementation", "The framework must be embedded in locally legible and life-stage-responsive ways rather than copied mechanically.", "Secondary"),
        ],
        "cross_day": "The cross-day conclusion for `Q7` is that practical integration means redesign. Childhood points to structured awareness and family/community supports, youth to trust-building and accessible communication channels, adulthood to training and system reorganization, and older age to institutional embedding, dignity-sensitive spaces, and professional development. The practical layer across D1-D4 therefore converges not on one program, but on a redesign logic: whole-person care becomes more real when institutions, pathways, communication, and community linkages are deliberately built around it.",
    },
}

PLAIN_LANGUAGE_ANSWERS = {
    "Q1": {
        "CASE_D1": "In the childhood discussion, wellbeing was mainly described as balance, contentment, spiritual steadiness, and supportive care around the child.",
        "CASE_D2": "In the youth discussion, wellbeing was mainly described as balance, purpose, self-respect, and supportive relationships.",
        "CASE_D3": "In the adult discussion, wellbeing was mainly described as balance, coping, and inner steadiness under work and family pressure.",
        "CASE_D4": "In the elderly discussion, wellbeing was mainly described as peace, faith, dignity, and staying valued even when health is limited.",
    },
    "Q2": {
        "CASE_D1": "In the childhood discussion, being well meant more than having no symptoms; it meant balanced functioning in context.",
        "CASE_D2": "In the youth discussion, being well meant functioning, coping, and staying connected, even when distress might be hidden.",
        "CASE_D3": "In the adult discussion, being well meant holding responsibilities, values, and daily life together, not simply being physically okay.",
        "CASE_D4": "In the elderly discussion, being well meant dignity, autonomy, emotional steadiness, and support, not just looking calm.",
    },
    "Q3": {
        "CASE_D1": "In the childhood discussion, the pillars improved wellbeing when children were supported through family, schools, clinics, and early awareness.",
        "CASE_D2": "In the youth discussion, the pillars improved wellbeing by strengthening belonging, support, identity, and emotional regulation.",
        "CASE_D3": "In the adult discussion, the pillars improved wellbeing when self-care could be balanced with work, family, and system support.",
        "CASE_D4": "In the elderly discussion, the pillars improved wellbeing when ageing was supported through dignity, social value, faith, and practical care.",
    },
    "Q4": {
        "CASE_D1": "In the childhood discussion, current services showed some whole-person care, but much of the system still felt fragmented and narrow.",
        "CASE_D2": "In the youth discussion, services partly reflected the pillars, but pressure and waiting often pushed wider wellbeing aside.",
        "CASE_D3": "In the adult discussion, services helped physically, but often failed to support explanation, navigation, and life beyond the visit.",
        "CASE_D4": "In the elderly discussion, some holistic practices were present, but not in a consistent system-wide way.",
    },
    "Q5": {
        "CASE_D1": "In the childhood discussion, the main barriers were weak coordination, limited listening, and poor inclusion around the child.",
        "CASE_D2": "In the youth discussion, the main barriers were disclosure risk, stigma, time pressure, and weak youth-safe trust.",
        "CASE_D3": "In the adult discussion, the main barriers were hierarchy, navigation difficulty, and limited time for real explanation.",
        "CASE_D4": "In the elderly discussion, the main barriers were staffing pressure, language mismatch, and the difficulty of turning dignity into routine practice.",
    },
    "Q6": {
        "CASE_D1": "In the childhood discussion, the clearest opening for change was the school system and earlier awareness.",
        "CASE_D2": "In the youth discussion, the clearest openings were school nurses, parents, and earlier youth support structures.",
        "CASE_D3": "In the adult discussion, the clearest openings were accessible counselling, public awareness, and cross-sector support.",
        "CASE_D4": "In the elderly discussion, the clearest openings were home care, awareness work, and careful use of technology.",
    },
    "Q7": {
        "CASE_D1": "In the childhood discussion, practical change centred on schools, family support, workforce training, and community-based child wellbeing supports.",
        "CASE_D2": "In the youth discussion, practical change centred on safer communication routes, awareness, and trust-building supports.",
        "CASE_D3": "In the adult discussion, practical change centred on redesigning care pathways, training, and institution-level adoption of the pillars.",
        "CASE_D4": "In the elderly discussion, practical change centred on dignity-focused redesign, communication training, and elder-specific social-health supports.",
    },
}

QUESTION_MEANING = {
    "Q1": "This shows that wellbeing is understood as a broad moral and relational condition, not simply as comfort or the absence of illness.",
    "Q2": "This shows that judging whether someone is well requires more than checking symptoms or outward appearance.",
    "Q3": "This shows that the HT framework is being understood as a connected social model rather than as five separate boxes.",
    "Q4": "This shows the gap between the wellbeing ideal described by participants and the reality of current service delivery.",
    "Q5": "This shows that the main barriers to whole-person care lie in the organization of care, not in the value of the framework itself.",
    "Q6": "This shows that meaningful change can start from institutions and practices that already exist rather than waiting for a completely new system.",
    "Q7": "This shows that participants can translate the HT framework into practical service design, training priorities, and institutional standards.",
}

QUESTION_IMPORTANCE = {
    "Q1": "This matters because it sets the benchmark for the rest of the report. If wellbeing is defined this broadly, healthcare cannot be judged only by fast symptom relief.",
    "Q2": "This matters because it changes how healthcare should assess need. A narrow clinical reading would miss many of the conditions participants treat as central to real wellbeing.",
    "Q3": "This matters because it demonstrates that the HT framework has practical meaning for participants and is not simply aspirational language.",
    "Q4": "This matters because it identifies where healthcare falls short of the whole-person standard that participants themselves set earlier in the workshops.",
    "Q5": "This matters because it points reform efforts toward the real points of blockage: time, hierarchy, fragmentation, explanation, trust, and coordination.",
    "Q6": "This matters because it suggests that reform can begin by strengthening and connecting opportunities that are already visible in the system.",
    "Q7": "This matters because it moves the framework from principle into implementation and shows what participants believe real integration would require.",
}

QUESTION_TENSIONS = {
    "Q1": "A key tension here is between peace/contentment and balance/functioning. Another is between an individual account of wellbeing and a relational account carried by family, caregivers, and institutions.",
    "Q2": "A key tension here is between visible functioning and hidden distress. Another is between independence and the continuing need for relational or institutional support.",
    "Q3": "A key tension here is between personal effort and system support. Another is between treating all five pillars as equally important in theory and weighting them differently in practice.",
    "Q4": "A key tension here is between pockets of good practice and the absence of consistent system-wide integration. Another is between strong physical care and weaker support for the other pillars.",
    "Q5": "A key tension here is between professional goodwill and system constraint. Another is between asking patients to take responsibility and building services that make such responsibility realistic.",
    "Q6": "A key tension here is between visible opportunities and weak coordination. Another is between enthusiasm for change and unequal readiness across settings and life stages.",
    "Q7": "A key tension here is between ambitious redesign and the uneven depth of late-question material in some cases. Another is between standardized reform and the need for life-stage-sensitive adaptation.",
}

STAGE_CONTEXT = {
    "CASE_D1": "In childhood, these issues are often interpreted through caregivers, professionals, schools, and the systems around the child rather than through child voice alone.",
    "CASE_D2": "In youth, these issues are closely tied to identity, belonging, peer life, stigma, and the safety of disclosure.",
    "CASE_D3": "In adulthood, these issues are tested by work, caregiving, competing roles, and pressure to keep functioning.",
    "CASE_D4": "In older age, these issues are shaped by dignity, non-burden, autonomy, support, and continued social significance.",
}

HT_STAGE_RELEVANCE = {
    "CASE_D1": "For the HT framework, this means childhood wellbeing cannot be carried by the child alone; it depends on whether family, school, and service environments support the five pillars together.",
    "CASE_D2": "For the HT framework, this means youth wellbeing depends not only on inner balance but also on safe belonging, trusted relationships, and socially credible support.",
    "CASE_D3": "For the HT framework, this means adult wellbeing must be understood inside work, family, and role pressure rather than as a purely private achievement.",
    "CASE_D4": "For the HT framework, this means elder wellbeing must be read through dignity, relational worth, and meaningful support rather than through decline alone.",
}

CROSS_DAY_PLAIN = {
    "Q1": "Across the four days, wellbeing was described as a balanced and meaningful life rather than a trouble-free life.",
    "Q2": "Across the four days, being well meant more than being symptom-free or appearing calm on the surface.",
    "Q3": "Across the four days, the five pillars improved wellbeing when they worked together rather than in isolation.",
    "Q4": "Across the four days, healthcare reflected the pillars only partly and unevenly.",
    "Q5": "Across the four days, the main barriers were structural and relational rather than conceptual.",
    "Q6": "Across the four days, useful openings for change already existed but were scattered and unevenly connected.",
    "Q7": "Across the four days, practical integration was described as a matter of redesign rather than goodwill alone.",
}

CROSS_DAY_HT_RELEVANCE = {
    "Q1": "For the HT framework, this means the five pillars are being used as a broad definition of the good life before healthcare is discussed at all.",
    "Q2": "For the HT framework, this means real assessment must look across the pillars rather than using narrow biomedical signs as the main guide.",
    "Q3": "For the HT framework, this means participants understand the pillars as an interdependent model that must fit life stage and social context.",
    "Q4": "For the HT framework, this means the central challenge is not framework acceptance but weak institutional embedding.",
    "Q5": "For the HT framework, this means whole-person care is blocked mainly by system design, not by lack of conceptual clarity.",
    "Q6": "For the HT framework, this means implementation can begin by connecting existing institutions to the five-pillar logic more deliberately.",
    "Q7": "For the HT framework, this means participants are already describing what practical integration should look like in training, pathways, standards, and community linkage.",
}

CROSS_DAY_TENSIONS = {
    "Q1": "The main cross-day tension is between defining wellbeing as inner peace and defining it as balance across domains, with each life stage weighting the two differently.",
    "Q2": "The main cross-day tension is between what looks visible and what is actually experienced, especially when distress is hidden for social or relational reasons.",
    "Q3": "The main cross-day tension is between the ideal of equally valued pillars and the practical reality that some pillars carry more weight at different life stages.",
    "Q4": "The main cross-day tension is between individual examples of good care and the lack of a stable whole-system model.",
    "Q5": "The main cross-day tension is between asking people to navigate the system well and building a system that is actually navigable, trustworthy, and coordinated.",
    "Q6": "The main cross-day tension is between the presence of useful entry points and the weakness of the links between them.",
    "Q7": "The main cross-day tension is between broad agreement on what should change and the uneven practical detail available across the life stages.",
}

CROSS_DAY_STAGE_SHIFT = {
    "Q1": "The emphasis shifts from safety and supported balance in childhood, to identity and usefulness in youth, to coping under role pressure in adulthood, and to dignity-preserving peace in older age.",
    "Q2": "The emphasis shifts from contextual judgement in childhood, to hidden distress in youth, to responsibility under pressure in adulthood, and to dignity-sensitive assessment in older age.",
    "Q3": "The emphasis shifts from support ecology in childhood, to belonging and identity in youth, to system-supported balance in adulthood, and to dignified ageing in older age.",
    "Q4": "The emphasis shifts from fragmented child-service ecology, to pressured youth care, to adult explanation and navigation gaps, and to patchy elder-care integration.",
    "Q5": "The emphasis shifts from coordination and listening problems, to trust and stigma, to hierarchy and navigation barriers, and to the difficulty of embedding dignity in routine care.",
    "Q6": "The emphasis shifts from school entry points, to youth support infrastructures, to counselling and public awareness, and to home care and carefully used technology.",
    "Q7": "The emphasis shifts from school and family supports, to youth-safe communication, to institution-level adult-care redesign, and to elder-specific dignity-focused redesign.",
}

QUESTION_TEXT_SIGNALS = {
    "Q1": ["wellbeing", "well-being", "الحياة", "طيبة", "content", "balance", "happy", "meaningful", "spiritual", "social", "physical", "emotional", "holistic", "purpose", "giving", "receiving", "work", "home", "mother", "child", "teenager", "قناعة", "راضي", "رضا", "سلام", "مرتاح"],
    "Q2": ["wellness", "well", "بعافية", "عافية", "function", "cope", "productive", "peace", "support", "burden", "360", "hidden"],
    "Q3": ["pillar", "pillars", "ركائز", "improve", "improving", "responsibility", "system", "support", "dignity"],
    "Q4": ["service", "services", "care", "clinic", "healthcare", "appointment", "wait", "time", "institution", "خدمات", "الرعاية"],
    "Q5": ["challenge", "barrier", "trust", "time", "pressure", "communication", "hierarchy", "stigma", "language", "تحديات"],
    "Q6": ["opportunity", "school", "home care", "awareness", "campaign", "technology", "access", "فرص"],
    "Q7": ["suggestion", "proposal", "training", "campaign", "integrate", "licensing", "redesign", "اقتراح", "تدريب", "دمج"],
}

FRIENDLY_ROLE_LABELS = {
    "Unclear speaker identity cluster": "participant contribution with incomplete speaker attribution",
}


def build_deep_life_course_report(
    case_packages: dict[str, dict[str, Any]],
    question_totals: list[dict[str, str]],
    matrix_rows: list[dict[str, str]],
) -> str:
    """Build a deeper integrated life-course report from outward-facing evidence.

    Args:
        case_packages: Loaded outward-facing case package data keyed by case ID.
        question_totals: Integrated question total rows.
        matrix_rows: Integrated question-theme matrix rows.

    Returns:
        The detailed integrated markdown report.
    """
    total_segments = sum(int(row["participant_segments"]) for row in question_totals)
    lines = [
        "# Life-Course Wellbeing Focus Groups",
        "",
        "## Full Thematic Analysis Report",
        "",
        "### Childhood • Youth • Adults • Elderly",
        "",
        "Prepared for the Health Sector Workshop Series  ",
        "Date: March 12, 2026",
        "",
        "---",
        "",
        "## Executive Summary",
        "This report brings together four life-course focus group workshops: Childhood, Youth, Adults, and Elderly. It is organized around the moderators’ seven discussion questions rather than around the cases alone, so each question shows what was said at each life stage and what the wider pattern becomes when the four days are read together.",
        "",
        f"Across the seven questions, the report draws on `{total_segments}` participant segments. The richest conceptual discussion appears in `Q3`, where participants explain most clearly how the five pillars can improve wellbeing. The strongest system critique appears in `Q4` and `Q5`, where all four days describe healthcare as only partly able to support the whole-person model they value.",
        "",
        "The HT framework presents `الحياة الطيبة` as a holistic and value-based way of thinking about life through five connected pillars: spiritual, emotional, intellectual, physical, and social. Read through that lens, the four workshops tell a consistent story. Wellbeing is understood as multidimensional, relational, and larger than symptom control. What changes across childhood, youth, adulthood, and older age is the social setting that carries wellbeing, the kind of pressure that threatens it, and the kind of change participants believe healthcare needs.",
        "",
        "## Methodology",
        "This synthesis draws on the final case reports, excerpt collections, question-theme matrices, summary tables, prominence tables, participant outputs, and the integrated D1-D4 synthesis materials. Raw transcripts and internal identity files were not reopened for this report.",
        "",
        "The study materials distinguish between verbatim transcript quotations, note-style summaries, note-taker summaries, close-reading support, and auxiliary recommendation material. This report keeps those distinctions visible instead of presenting every piece of material as the same kind of evidence. Arabic remains authoritative where Arabic is the source language, and English quotations are kept where they appear in the study materials.",
        "",
        "The original case reports were written before the HT framework document was fully integrated into this synthesis. This report therefore re-reads the four workshops through the HT framework so that the five pillars guide interpretation without changing the underlying evidence.",
        "",
        "## HT framework orientation for this report",
        "- **Framework definition**: `الحياة الطيبة` is treated as an integrated form of flourishing across the spiritual, emotional, intellectual, physical, and social pillars.",
        "- **Interdependence rule**: The pillars are read as mutually shaping one another rather than as independent checklist items.",
        "- **Value clusters from the framework**: The PDF aligns the pillars with clusters such as care/cooperation/responsibility, health/strength/prevention, truth/wisdom/reflection, balance/determination/emotional refinement, and spiritual cultivation.",
        "- **Interpretive rule**: The integrated report tracks how the same HT framework is weighted differently across childhood, youth, adulthood, and older age rather than assuming identical emphasis in every case.",
        "",
        "## How theme weights were assigned",
        "- **Frequency**: How often a pattern recurred across the question analyses, matrices, and supporting quotations.",
        "- **Diversity**: Whether the pattern appeared across multiple life stages, multiple speaker positions, and more than one source or table.",
        "- **Depth**: The richness of the discussion, including explanatory detail, emotional force, and system specificity rather than simple repetition alone.",
        "",
        "Weights used in this report:",
        "- **Primary**: Dominant and cross-day recurrent",
        "- **Secondary**: Recurring and analytically strong, but not as dominant as the primary layer",
        "- **Emerging**: Present and meaningful, but narrower in spread, density, or evidential reach",
        "",
        "## Findings by Moderators’ Questions",
        "",
    ]
    for question_id in QUESTION_ORDER:
        if question_id in QUESTION_PART:
            lines.extend([QUESTION_PART[question_id], ""])
        lines.extend(_render_question(case_packages, question_totals, matrix_rows, question_id))
    lines.extend(
        [
            "## Cross-Day Thematic Overview",
            "- **The five-pillar HT model is the stable conceptual core**: Across all four days, `الحياة الطيبة` is read as multidimensional balance across spiritual, emotional, intellectual, physical, and social life rather than as simple symptom absence.",
            "- **Surface stability is an unreliable indicator**: Youth, adults, and elderly discussions all warn that calm appearance or visible functioning can conceal distress, burden, or unmet need; the childhood case raises the same caution through the theme of hidden distress and unreliable appearances.",
            "- **The social ecology changes across the life course**: Childhood is framed through professional-family support ecologies, youth through peer and disclosure worlds, adulthood through role-bearing strain, and older age through dignity, non-burden, and social recognition.",
            "- **Current services remain partial and uneven**: The strongest integrated service-facing pattern is that healthcare still over-concentrates on the physical pillar while relational, communicative, social, spiritual, and wider whole-person dimensions are inconsistently embedded.",
            "- **Fragmentation and time pressure are cross-day barriers**: Short encounters, weak continuity, hierarchy, explanation gaps, and uneven navigation recur in every day, though they are experienced differently at each life stage.",
            "- **Redesign logic is institutionally focused rather than purely interpersonal**: Participants repeatedly ask for embedded standards, training, communication reform, earlier prevention, stronger community linkage, and service models that do not rely on individual goodwill alone.",
            "",
            "## Policy Implications",
            "1. Adopt a holistic wellbeing framework as a service standard rather than treating it as an optional or informal add-on.",
            "2. Redesign care pathways so that physical, mental, social, family, and community supports can be coordinated rather than left fragmented across separate encounters.",
            "3. Protect the relational conditions of care by addressing time pressure, explanation quality, continuity, and the patient’s safety to disclose sensitive distress.",
            "4. Build prevention and early-intervention partnerships across life stages, especially through schools, families, community settings, and publicly understandable awareness structures.",
            "5. Treat workforce support, communication training, quality indicators, and culturally grounded practice as quality-of-care issues rather than optional professional extras.",
            "6. Embed dignity-sensitive, life-stage-responsive care standards so that childhood, youth, adulthood, and older age are not folded into one generic model of need.",
            "",
            "## Study Limits",
            "This report keeps the main limits of the four case studies in view. These include the thinner late-question material in Day 1, note-supported material in parts of Day 2, attribution and late-question caution in Day 3, and the granularity and merged-late-section caution in Day 4.",
            "",
        ]
    )
    return "\n".join(lines)


def _render_question(
    case_packages: dict[str, dict[str, Any]],
    question_totals: list[dict[str, str]],
    matrix_rows: list[dict[str, str]],
    question_id: str,
) -> list[str]:
    content = QUESTION_CONTENT[question_id]
    lines = [
        f"### {question_id}. {content['title']}",
        content["arabic"],
        "",
        _integrated_profile(question_totals, matrix_rows, question_id),
        content["intro"],
        "",
        "#### Detailed findings by life stage",
    ]
    for case_id in CASE_LABELS:
        lines.extend(_render_case_block(case_packages, case_id, question_id, content["cases"][case_id]))
    lines.extend([
        "#### Key themes",
        *_table(content["themes"], ["Theme", "Summary", "Weight"]),
        "",
        "#### Cross-day synthesis",
        "###### Plain-language answer",
        CROSS_DAY_PLAIN[question_id],
        "",
        "###### What the four days show together",
        content["cross_day"],
        "",
        "###### Why this matters for the HT framework",
        CROSS_DAY_HT_RELEVANCE[question_id],
        "",
        "###### Cross-day tensions and nuances",
        CROSS_DAY_TENSIONS[question_id],
        "",
        "###### Cross-day analytic snapshot",
        *_table(_cross_day_snapshot_rows(case_packages, matrix_rows, question_id), ["Element", "Summary"]),
        *_cross_day_patterns(case_packages, matrix_rows, question_id),
        "",
    ])
    return lines


def _render_case_block(
    case_packages: dict[str, dict[str, Any]],
    case_id: str,
    question_id: str,
    summary: str,
) -> list[str]:
    label = CASE_LABELS[case_id]
    package = case_packages[case_id]
    question_row = next(row for row in package["question_evidence"] if row["question_id"] == question_id)
    report_material = _extract_case_report_material(package, case_id, question_id)
    coded_segment_rows = _select_coded_segment_rows(package["coded_segments"], question_id, question_row["top_codes"])
    coded_quote_blocks = [_format_coded_segment_quote_block(case_id, row, package["excerpt_bank"]) for row in coded_segment_rows]
    excerpt_rows = _select_excerpt_rows(
        [row for row in package["excerpt_bank"] if row["question_id"] == question_id],
        question_row["top_codes"],
        question_id,
    )
    quote_blocks = _merge_quote_blocks(report_material["quotes"], coded_quote_blocks, excerpt_rows, case_id)
    evidence_mix = Counter(row["evidence_type"] for row in excerpt_rows)
    theme_links = _case_theme_links(package, question_id)
    analytic_tension = _build_case_tension(question_id, case_id)
    lines = [
        f"##### {label}",
        "###### Plain-language answer",
        PLAIN_LANGUAGE_ANSWERS[question_id][case_id],
        "",
        "###### What participants were mainly saying",
        _build_main_saying(summary, question_row["top_codes"], excerpt_rows, report_material["analysis"]),
        "",
        "###### Raw quotations from different participants",
    ]
    if quote_blocks:
        for quote_text, attribution in quote_blocks:
            lines.extend(
                [
                    f"> {quote_text}",
                    f"> `{attribution}`",
                    "",
                ]
            )
    else:
        lines.append("No direct quotation excerpt is preserved for this question. Where relevant, practical or supporting material remains reflected in the case summary above without being presented as verbatim quotation evidence.")
        lines.append("")
    lines.extend([
        "###### What this means",
        _build_case_meaning(question_id, case_id, report_material["significance"]),
        "",
        "###### Why this matters for the HT framework",
        _build_case_importance(question_id, case_id, report_material["significance"]),
        "",
        "###### Tensions and nuances",
        analytic_tension,
        "",
        "###### Linked themes",
        *_theme_link_lines(theme_links),
        "",
        "###### Analytic snapshot",
        *_table(
            _case_snapshot_rows(
                package=package,
                question_id=question_id,
                question_row=question_row,
                excerpt_rows=excerpt_rows,
                quote_blocks=quote_blocks,
                theme_links=theme_links,
                analytic_tension=analytic_tension,
            ),
            ["Element", "Summary"],
        ),
        "",
    ])
    return lines


def _integrated_profile(question_totals: list[dict[str, str]], matrix_rows: list[dict[str, str]], question_id: str) -> str:
    totals = next(row for row in question_totals if row["question_id"] == question_id)
    matrix = next(row for row in matrix_rows if row["question_id"] == question_id)
    theme_values = {
        "IT1": int(matrix["IT1_segments"]),
        "IT2": int(matrix["IT2_segments"]),
        "IT3": int(matrix["IT3_segments"]),
        "IT4": int(matrix["IT4_segments"]),
    }
    top_value = max(theme_values.values())
    dominant = ", ".join(THEME_LABELS[key] for key, value in theme_values.items() if value == top_value)
    return (
        f"**Integrated evidence profile:** `{totals['participant_segments']}` participant segments, "
        f"`{totals['summed_unique_participant_speakers']}` summed participant-speaker counts, "
        f"dominant integrated theme(s): `{dominant}`."
    )


def _build_main_saying(
    summary: str,
    top_codes: str,
    excerpt_rows: list[dict[str, str]],
    report_analysis: str,
) -> str:
    if report_analysis:
        return report_analysis
    pattern_clause = _build_pattern_clause(top_codes)
    voices = _format_supporting_voices(excerpt_rows)
    sentence = summary
    if pattern_clause:
        sentence += f" The clearest response patterns in this part of the discussion were {pattern_clause}."
    if voices:
        sentence += f" These points were especially visible in comments from {voices}."
    return sentence


def _build_case_meaning(question_id: str, case_id: str, report_significance: str) -> str:
    if report_significance:
        return f"{report_significance} {STAGE_CONTEXT[case_id]}"
    return f"{QUESTION_MEANING[question_id]} {STAGE_CONTEXT[case_id]}"


def _build_case_importance(question_id: str, case_id: str, report_significance: str) -> str:
    if report_significance:
        return f"{QUESTION_IMPORTANCE[question_id]} {HT_STAGE_RELEVANCE[case_id]}"
    return f"{QUESTION_IMPORTANCE[question_id]} {HT_STAGE_RELEVANCE[case_id]}"


def _build_case_tension(question_id: str, case_id: str) -> str:
    return f"{QUESTION_TENSIONS[question_id]} {STAGE_CONTEXT[case_id]}"


def _extract_case_report_material(
    package: dict[str, Any],
    case_id: str,
    question_id: str,
) -> dict[str, Any]:
    section_text = _extract_case_report_section(package["report_text"], question_id)
    if not section_text:
        return {"analysis": "", "significance": "", "quotes": []}

    quotes: list[tuple[str, str]] = []
    paragraphs: list[str] = []
    current_paragraph: list[str] = []
    significance = ""

    for raw_line in section_text.splitlines():
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("### "):
            if current_paragraph:
                paragraphs.append(" ".join(current_paragraph).strip())
                current_paragraph = []
            continue
        if stripped == "---":
            if current_paragraph:
                paragraphs.append(" ".join(current_paragraph).strip())
                current_paragraph = []
            continue
        if stripped.startswith("**") and "participant segments" in stripped.lower():
            continue
        if stripped.startswith(">"):
            if current_paragraph:
                paragraphs.append(" ".join(current_paragraph).strip())
                current_paragraph = []
            quote_block = _format_report_quote_block(package["excerpt_bank"], case_id, stripped[1:].strip())
            if quote_block:
                quotes.append(quote_block)
            continue
        if stripped.startswith("**Analytical significance**:"):
            if current_paragraph:
                paragraphs.append(" ".join(current_paragraph).strip())
                current_paragraph = []
            significance = _simplify_internal_terms(_strip_bold_markup(stripped.split(":", 1)[1].strip()))
            continue
        current_paragraph.append(_simplify_internal_terms(_strip_bold_markup(stripped)))

    if current_paragraph:
        paragraphs.append(" ".join(current_paragraph).strip())

    analysis = "\n\n".join(paragraph for paragraph in paragraphs if paragraph)
    return {"analysis": analysis, "significance": significance, "quotes": quotes}


def _extract_case_report_section(report_text: str, question_id: str) -> str:
    question_number = QUESTION_ORDER.index(question_id) + 1
    match = re.search(
        rf"^### 3\.{question_number} .*?(?=^### 3\.\d+ |^## |^# |\Z)",
        report_text,
        flags=re.MULTILINE | re.DOTALL,
    )
    return match.group(0).strip() if match else ""


def _format_report_quote_block(
    excerpt_bank: list[dict[str, str]],
    case_id: str,
    raw_quote_line: str,
) -> tuple[str, str] | None:
    quote_text, separator, metadata = raw_quote_line.partition(" — ")
    quote_text = quote_text.strip()
    if not quote_text:
        return None
    evidence_id_match = re.search(r"\bD\d_[SE]\d+\b", raw_quote_line)
    if evidence_id_match:
        evidence_id = evidence_id_match.group(0)
        matched_row = next((row for row in excerpt_bank if row["evidence_id"] == evidence_id), None)
        if matched_row is not None:
            return (quote_text, _format_evidence_label(case_id, matched_row))
    simplified_metadata = _simplify_quote_metadata(metadata if separator else raw_quote_line)
    if simplified_metadata:
        return (quote_text, f"{CASE_LABELS[case_id]} · {simplified_metadata}")
    return (quote_text, CASE_LABELS[case_id])


def _simplify_quote_metadata(metadata: str) -> str:
    text = metadata.strip()
    if not text:
        return ""
    text = re.sub(r"\bD\d+_P\d+\b,?\s*", "", text)
    text = re.sub(r"\bD\d+_U\d+\b,?\s*", "", text)
    text = re.sub(r"\bHW[A-Z]+\d+[A-Z0-9]+\b,?\s*", "", text)
    text = re.sub(r"\bD\d_[SE]\d+\b", "", text)
    text = text.replace("[", "").replace("]", "")
    text = text.replace("coded transcript support", "verbatim transcript")
    text = text.replace("note-taker record", "note-taker summary")
    for raw_label, friendly_label in FRIENDLY_ROLE_LABELS.items():
        text = text.replace(raw_label, friendly_label)
    text = re.sub(r",\s*,", ", ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip(" ,")


def _strip_bold_markup(text: str) -> str:
    return re.sub(r"\*\*(.+?)\*\*", r"\1", text)


def _simplify_internal_terms(text: str) -> str:
    simplified = text
    replacements = {
        "outward-facing ": "",
        "evidence layer": "evidence",
        "excerpt-bank": "evidence",
        "cross-cutting": "cross-day",
        "coded transcript support": "verbatim transcript",
        "note-supported": "note-supported",
        "`": "",
        "HWAD6AR": "one late adult source",
        "HWAD10AR": "one adult source",
        "HWAD4AR": "one Arabic adult source",
        "HWEL10AR": "one late English elder source",
        "HWEL9AR": "one granular Arabic elder source",
        "unclear": "incompletely attributed",
        "participant-coded sections": "sections where speakers are more clearly attributable",
        "attribution-cautious": "cautious about individual speaker attribution",
        "recommendation workbook": "structured recommendation sheet",
        "auxiliary material": "supporting material",
        "transcript-equivalent evidence": "direct quotation evidence",
        "transcript-equivalent theme evidence": "direct quotation evidence",
        "Q6-coded evidence rows": "the clearest Q6 material",
        "excerpt bank": "evidence collection",
        "general_response": "broad general discussion",
        "Auxiliary structured recommendation sheet [auxiliary]:": "Supportive recommendation material:",
        "The Health_Workshop_Suggestions Day 1.xlsx workbook contains 40 structured practical suggestions from Day 1 participants.": "A structured Day 1 recommendation sheet preserves 40 practical suggestions from participants.",
        "evidence excerpts": "supporting quotations",
    }
    for old, new in replacements.items():
        simplified = simplified.replace(old, new)
    simplified = re.sub(r"\bHW[A-Z]+\d+[A-Z0-9]+\b", "one source", simplified)
    simplified = re.sub(r"\(D\d_[SE]\d+\)", "", simplified)
    phrase_replacements = {
        "the weak one source Q2/Q3 boundary remains important here.": "the weak boundary between Q2 and Q3 in part of the early adult material remains important here.",
        "The strongest Q2 evidence comes from one adult source and one Arabic adult source, not from assuming that every early Day 3 source preserves the question equally cleanly.": "The strongest Q2 evidence comes from the clearer English and Arabic adult sources rather than from assuming that every early Day 3 source preserves the question equally clearly.",
        "Because one source preserves Q3 less cleanly than one source, one Arabic adult source, and one adult source, the strongest Day 3 Q3 interpretation rests on those cleaner sources.": "Because one early adult source preserves Q3 less cleanly than the stronger Arabic and English adult sources, the strongest Day 3 Q3 interpretation rests on those cleaner sections.",
        "An important Arabic echo appears in one Arabic adult source, where one participant says that the specialist \"لا يعرف يشرح five different aspects\", reinforcing the same problem from another source:": "An important Arabic echo appears in a clearer Arabic adult source, where one participant says that the specialist \"لا يعرف يشرح five different aspects\", reinforcing the same problem seen elsewhere:",
        "The weak one adult source Q6 preservation means the strongest direct Q6 opportunity material comes from one Arabic adult source and narrower supporting material elsewhere.": "Because one adult source does not preserve Q6 clearly, the strongest direct Q6 opportunity material comes from a clearer Arabic adult source, with narrower supporting material elsewhere.",
        "Q6 is analytically useful but structurally uneven. The strongest opportunity talk comes from one source, one source, one granular Arabic elder source, and concise late English material in one late English elder source, which remains part of a merged Part 2 block rather than a fully clean standalone Q6 section.": "Q6 is analytically useful but structurally uneven. The strongest opportunity talk comes from several clearer elder sources, together with concise late English material that sits inside a merged later section rather than a fully clean standalone Q6 block.",
        "The strongest surviving practical-suggestion material comes from one late adult source, where late discussion is substantial but largely preserved as incompletely attributed rather than cleanly speaker-attributed transcript turns.": "The strongest surviving practical-suggestion material comes from later adult discussion where the material is substantial but not always attributable to individually named speakers.",
        "Yet the Q7 material still carries Day 4 caveats: some late English material is merged into a broader later section, and one granular Arabic elder source is disproportionately shaped by a small number of especially heavy contributors.": "Yet the Q7 material still carries Day 4 caveats: some late English material is merged into a broader later section, and one granular Arabic elder source is disproportionately shaped by a small number of especially heavy contributors.",
        "The excerpt bank also places additional Q4 Theme 3 evidence in one source, where participants describe weak follow-up, poor coordination, and missing child-focused services across otherwise connected institutions.": "Additional Q4 Theme 3 evidence appears in one childhood source, where participants describe weak follow-up, poor coordination, and missing child-focused services across otherwise connected institutions.",
        "Q6 has limited coded theme matches (only 5 segments mapped to Themes 2 and 3; zero mapped to Themes 1 and 4) because 60 of 65 participant segments are coded as general_response. The analytical content described below is based on close reading of the segment text, not automated code-to-theme mapping.": "Q6 is a thinner and more diffuse part of the childhood discussion. Much of this material survives as broad opportunity talk rather than tightly clustered theme evidence, so the interpretation below relies more on close reading of participant discussion.",
        "Q7 has the smallest evidence base in the transcripts and zero coded theme matches (all 21 segments coded as general_response). The excerpt bank contains no Q7 excerpt rows, so this section does not reuse transcript quotations from other questions. The evidence for Q7 is therefore limited to the auxiliary recommendation workbook, which is clearly labeled and not treated as transcript-equivalent theme evidence.": "Q7 has the thinnest direct discussion in the childhood case. The clearest surviving material is practical suggestion content rather than dense thematic discussion, and this section therefore draws on clearly labeled supportive implementation material rather than treating it as direct participant quotation.",
        "Auxiliary recommendation workbook [auxiliary]: The Health_Workshop_Suggestions Day 1.xlsx workbook contains 40 structured practical suggestions from Day 1 participants.": "Supportive recommendation material: A structured Day 1 recommendation sheet preserves 40 practical suggestions from participants.",
        "Q7 has the smallest evidence base in the transcripts and zero coded theme matches (all 21 segments coded as broad general discussion). The evidence collection contains no Q7 excerpt rows, so this section does not reuse transcript quotations from other questions. The evidence for Q7 is therefore limited to the auxiliary structured recommendation sheet, which is clearly labeled and not treated as direct quotation evidence.": "Q7 has the thinnest direct discussion in the childhood case. The clearest surviving material is practical suggestion content rather than dense thematic discussion, and this section therefore draws on clearly labeled supportive implementation material rather than treating it as direct participant quotation.",
        "Auxiliary structured recommendation sheet [auxiliary]: The Health_Workshop_Suggestions Day 1.xlsx workbook contains 40 structured practical suggestions from Day 1 participants.": "Supportive recommendation material: A structured Day 1 recommendation sheet preserves 40 practical suggestions from participants.",
        "Broader opportunity ideas elsewhere in the case — culturally informed implementation, stronger community awareness, and support for healthcare workers — remain analytically relevant to Theme 4, but they do not appear as the clearest Q6 material in the evidence.": "Broader opportunity ideas elsewhere in the case — culturally informed implementation, stronger community awareness, and support for healthcare workers — remain analytically relevant to Theme 4, but they are less directly preserved in the main Q6 material.",
        "The evidence collection also places additional Q4 Theme 3 evidence in one source, where participants describe weak follow-up, poor coordination, and missing child-focused services across otherwise connected institutions.": "Additional Q4 Theme 3 evidence appears in one childhood source, where participants describe weak follow-up, poor coordination, and missing child-focused services across otherwise connected institutions.",
        "Q6 has limited coded theme matches (only 5 segments mapped to Themes 2 and 3; zero mapped to Themes 1 and 4) because 60 of 65 participant segments are coded as broad general discussion. The analytical content described below is based on close reading of the segment text, not automated code-to-theme mapping.": "Q6 is a thinner and more diffuse part of the childhood discussion. Much of this material survives as broad opportunity talk rather than tightly clustered theme evidence, so the interpretation below relies more on close reading of participant discussion.",
        "Auxiliary structured recommendation sheet [auxiliary]: The Health_Workshop_Suggestions Day 1.xlsx workbook contains 40 structured practical suggestions from Day 1 participants. Key recommendation categories include:": "Supportive recommendation material: A structured Day 1 recommendation sheet preserves 40 practical suggestions from participants. Key recommendation categories include:",
    }
    for old, new in phrase_replacements.items():
        simplified = simplified.replace(old, new)
    simplified = re.sub(r"\s+", " ", simplified)
    return simplified.strip()


def _merge_quote_blocks(
    report_quotes: list[tuple[str, str]],
    coded_quotes: list[tuple[str, str]],
    excerpt_rows: list[dict[str, str]],
    case_id: str,
    limit: int = 5,
) -> list[tuple[str, str]]:
    merged: list[tuple[str, str]] = []
    seen: set[str] = set()
    for quote_text, attribution in report_quotes:
        key = _normalize_quote_key(quote_text)
        if key in seen:
            continue
        seen.add(key)
        merged.append((quote_text, attribution))
        if len(merged) == limit:
            return merged
    for quote_text, attribution in coded_quotes:
        key = _normalize_quote_key(quote_text)
        if key in seen:
            continue
        seen.add(key)
        merged.append((quote_text, attribution))
        if len(merged) == limit:
            return merged
    for row in excerpt_rows:
        quote_text = row["excerpt_text"].strip()
        key = _normalize_quote_key(quote_text)
        if key in seen:
            continue
        seen.add(key)
        merged.append((quote_text, _format_evidence_label(case_id, row)))
        if len(merged) == limit:
            break
    return merged


def _normalize_quote_key(text: str) -> str:
    return re.sub(r"\W+", "", text).lower()


def _code_bullets(top_codes: str) -> list[str]:
    codes = [item for item in top_codes.split(";") if item]
    if len(codes) > 1:
        codes = [item for item in codes if item != "general_response"]
    return [f"- **{CODE_LABELS.get(code, code)}**" for code in codes] if codes else ["- **No coded signal list is preserved for this question row**"]


def _format_evidence_mix(evidence_mix: Counter[str]) -> str:
    if not evidence_mix:
        return "no direct quotation excerpts"
    return "; ".join(f"{EVIDENCE_TYPE_LABELS.get(key, key)}={value}" for key, value in sorted(evidence_mix.items()))


def _format_source_files(source_files: str) -> str:
    if ".docx" in source_files or ".xlsx" in source_files or ";" in source_files:
        file_count = len([item for item in source_files.split(";") if item])
        return f"{file_count} workshop source documents"
    return f"{source_files} workshop source documents"


def _format_evidence_label(case_id: str, row: dict[str, str]) -> str:
    role_label = _friendly_role_label(row["role_label"])
    evidence_label = EVIDENCE_TYPE_LABELS.get(row["evidence_type"], row["evidence_type"])
    if role_label.strip().lower() == evidence_label.strip().lower():
        return f"{CASE_LABELS[case_id]} · {evidence_label}"
    return f"{CASE_LABELS[case_id]} · {role_label} · {evidence_label}"


def _build_pattern_clause(top_codes: str) -> str:
    patterns = [CODE_LABELS.get(code, code).lower() for code in top_codes.split(";") if code and code != "general_response"]
    if not patterns:
        return "general response material"
    return _oxford_join(patterns[:4])


def _format_supporting_voices(excerpt_rows: list[dict[str, str]]) -> str:
    voices: list[str] = []
    seen: set[str] = set()
    for row in excerpt_rows:
        role_label = _friendly_role_label(row["role_label"]).strip()
        if not role_label or role_label in seen:
            continue
        seen.add(role_label)
        voices.append(role_label)
        if len(voices) == 4:
            break
    return _oxford_join(voices)


def _friendly_role_label(role_label: str) -> str:
    cleaned = role_label.strip()
    for raw_label, friendly_label in FRIENDLY_ROLE_LABELS.items():
        if raw_label in cleaned:
            return cleaned.replace(raw_label, friendly_label)
    return cleaned


def _format_top_codes(top_codes: str) -> str:
    codes = [CODE_LABELS.get(code, code) for code in top_codes.split(";") if code and code != "general_response"]
    return "; ".join(codes) if codes else "General response material"


def _theme_link_lines(theme_links: list[tuple[str, int]]) -> list[str]:
    if not theme_links:
        return ["- **No direct theme link could be ranked for this question block**"]
    lines = [f"- **Primary link**: `{theme_links[0][0]}`"]
    if len(theme_links) > 1:
        lines.append(f"- **Secondary link**: `{theme_links[1][0]}`")
    if len(theme_links) > 2:
        lines.append(f"- **Additional relevant theme**: `{theme_links[2][0]}`")
    return lines


def _case_theme_links(package: dict[str, Any], question_id: str) -> list[tuple[str, int]]:
    question_matrix_row = next(row for row in package["question_matrix"] if row["question_id"] == question_id)
    theme_links: list[tuple[str, int]] = []
    for key, value in question_matrix_row.items():
        if not key.endswith("_segments"):
            continue
        count = int(value)
        if count <= 0:
            continue
        theme_links.append((_format_case_theme_name(key.removesuffix("_segments")), count))
    return sorted(theme_links, key=lambda item: item[1], reverse=True)


def _format_case_theme_name(raw_name: str) -> str:
    parts = raw_name.split("_")
    if len(parts) >= 3 and parts[0] == "Theme":
        theme_number = parts[1]
        theme_label = " ".join(parts[2:])
        return f"Theme {theme_number} — {theme_label}"
    return raw_name.replace("_", " ")


def _case_snapshot_rows(
    package: dict[str, Any],
    question_id: str,
    question_row: dict[str, str],
    excerpt_rows: list[dict[str, str]],
    quote_blocks: list[tuple[str, str]],
    theme_links: list[tuple[str, int]],
    analytic_tension: str,
) -> list[tuple[str, str]]:
    quote_evidence_mix = _quote_block_evidence_mix(quote_blocks)
    quote_voices = _quote_block_voices(quote_blocks)
    return [
        ("Question focus", QUESTION_CONTENT[question_id]["title"]),
        (
            "Evidence base",
            f"{question_row['participant_segments']} participant segments; {question_row['unique_participant_speakers']} speakers; {_format_source_files(question_row['source_files'])}; {_format_evidence_mix(quote_evidence_mix)}",
        ),
        ("Main response patterns", _format_top_codes(question_row["top_codes"])),
        ("Supporting participant voices", quote_voices or _format_supporting_voices(excerpt_rows) or "Not specified in the selected quotations"),
        ("Linked themes", _oxford_join([theme_name for theme_name, _ in theme_links[:3]]) or "No ranked theme link available"),
        ("Analytic weight in this day", _relative_prominence(package["question_evidence"], question_id)),
        ("Divergence / tension", analytic_tension),
    ]


def _relative_prominence(question_rows: list[dict[str, str]], question_id: str) -> str:
    ordered = sorted(question_rows, key=lambda row: int(row["participant_segments"]), reverse=True)
    rank = next(index for index, row in enumerate(ordered, start=1) if row["question_id"] == question_id)
    if rank <= 2:
        return "Strong"
    if rank <= 5:
        return "Moderate"
    return "Focused"


def _quote_block_evidence_mix(quote_blocks: list[tuple[str, str]]) -> Counter[str]:
    mix: Counter[str] = Counter()
    for _, attribution in quote_blocks:
        if "note-style transcript summary" in attribution:
            mix["note_style_transcript_summary"] += 1
        elif "note-taker summary" in attribution:
            mix["note_taker_summary"] += 1
        elif "participant contribution" in attribution:
            mix["participant_contribution"] += 1
        elif "verbatim transcript" in attribution:
            mix["verbatim_transcript"] += 1
    return mix


def _quote_block_voices(quote_blocks: list[tuple[str, str]]) -> str:
    voices: list[str] = []
    seen: set[str] = set()
    for _, attribution in quote_blocks:
        parts = [part.strip() for part in attribution.split(" · ") if part.strip()]
        if len(parts) < 2:
            continue
        role_label = parts[1]
        if role_label in seen:
            continue
        seen.add(role_label)
        voices.append(role_label)
        if len(voices) == 4:
            break
    return _oxford_join(voices)


def _cross_day_snapshot_rows(
    case_packages: dict[str, dict[str, Any]],
    matrix_rows: list[dict[str, str]],
    question_id: str,
) -> list[tuple[str, str]]:
    matrix = next(row for row in matrix_rows if row["question_id"] == question_id)
    theme_values = {
        "IT1": int(matrix["IT1_segments"]),
        "IT2": int(matrix["IT2_segments"]),
        "IT3": int(matrix["IT3_segments"]),
        "IT4": int(matrix["IT4_segments"]),
    }
    dominant_themes = _oxford_join(
        [THEME_LABELS[key] for key, _ in sorted(theme_values.items(), key=lambda item: item[1], reverse=True)[:2]]
    )
    all_codes: list[str] = []
    evidence_types: Counter[str] = Counter()
    total_segments = 0
    total_speakers = 0
    for case_id in CASE_LABELS:
        question_row = next(row for row in case_packages[case_id]["question_evidence"] if row["question_id"] == question_id)
        total_segments += int(question_row["participant_segments"])
        total_speakers += int(question_row["unique_participant_speakers"])
        all_codes.extend(item for item in question_row["top_codes"].split(";") if item and item != "general_response")
        for row in _select_excerpt_rows(
            [item for item in case_packages[case_id]["excerpt_bank"] if item["question_id"] == question_id],
            question_row["top_codes"],
            question_id,
        ):
            evidence_types[row["evidence_type"]] += 1
    repeated_patterns = _oxford_join(
        [CODE_LABELS.get(code, code).lower() for code, _ in Counter(all_codes).most_common(5)]
    )
    return [
        ("Plain-language answer", CROSS_DAY_PLAIN[question_id]),
        ("Dominant integrated themes", dominant_themes),
        ("Life-stage shift", CROSS_DAY_STAGE_SHIFT[question_id]),
        ("Most repeated response patterns", repeated_patterns),
        ("Combined evidence depth", f"{total_segments} participant segments; {total_speakers} summed participant-speaker counts; {_format_evidence_mix(evidence_types)}"),
        ("Main tension", CROSS_DAY_TENSIONS[question_id]),
    ]


def _select_excerpt_rows(
    rows: list[dict[str, str]],
    top_codes: str,
    question_id: str,
    limit: int = 5,
) -> list[dict[str, str]]:
    unique_rows = _unique_excerpt_rows(rows)
    top_code_set = {code for code in top_codes.split(";") if code and code != "general_response"}
    evidence_score = {
        "verbatim_transcript": 3,
        "note_style_transcript_summary": 2,
        "note_taker_summary": 1,
        "close_reading_theme_support": 0,
    }
    scored_rows = sorted(
        unique_rows,
        key=lambda row: _excerpt_sort_key(row, top_code_set, evidence_score),
        reverse=True,
    )
    relevant_rows = [
        row
        for row in scored_rows
        if _excerpt_relevance_score(row, top_code_set) > 0
        and _question_text_fit(row["excerpt_text"], question_id)
    ]
    candidate_rows = relevant_rows if relevant_rows else scored_rows[:2]
    selected: list[dict[str, str]] = []
    seen_speakers: set[str] = set()
    for row in candidate_rows:
        speaker_key = row["speaker_code"] or row["role_label"]
        if speaker_key in seen_speakers and len(selected) < min(limit, len(candidate_rows)):
            continue
        seen_speakers.add(speaker_key)
        selected.append(row)
        if len(selected) == limit:
            return selected
    for row in candidate_rows:
        if row in selected:
            continue
        selected.append(row)
        if len(selected) == limit:
            break
    return selected


def _select_coded_segment_rows(
    rows: list[dict[str, str]],
    question_id: str,
    top_codes: str,
    limit: int = 3,
) -> list[dict[str, str]]:
    top_code_set = {code for code in top_codes.split(";") if code and code != "general_response"}
    candidate_rows = [
        row
        for row in rows
        if row["question_id"] == question_id
        and row["speaker_type"] == "participant"
        and _is_strong_segment_quote(row["segment_text"])
        and _excerpt_relevance_score({"codes": row["codes"]}, top_code_set) > 0
        and _question_text_fit(row["segment_text"], question_id)
    ]
    sorted_rows = sorted(
        candidate_rows,
        key=lambda row: (
            _question_signal_count(row["segment_text"], question_id),
            _excerpt_relevance_score({"codes": row["codes"]}, top_code_set),
            -abs(len(row["segment_text"].strip()) - 180),
        ),
        reverse=True,
    )
    selected: list[dict[str, str]] = []
    seen_speakers: set[str] = set()
    for row in sorted_rows:
        speaker_key = row["speaker_code"] or row["role_label"]
        if speaker_key in seen_speakers:
            continue
        seen_speakers.add(speaker_key)
        selected.append(row)
        if len(selected) == limit:
            break
    return selected


def _is_strong_segment_quote(text: str) -> bool:
    cleaned = text.strip()
    if len(cleaned) < 70:
        return False
    if len(cleaned.split()) < 10:
        return False
    if cleaned.lower().startswith(("yeah", "okay", "some,")):
        return False
    if any(
        phrase in cleaned.lower()
        for phrase in [
            "would you like to reconsider",
            "these are okay",
            "we can sign the consent",
            "you get a joke",
            "what specialty",
        ]
    ):
        return False
    return True


def _format_coded_segment_quote_block(
    case_id: str,
    row: dict[str, str],
    excerpt_bank: list[dict[str, str]],
) -> tuple[str, str]:
    matched_row = next(
        (
            excerpt_row
            for excerpt_row in excerpt_bank
            if excerpt_row["evidence_id"] == row["segment_id"] or excerpt_row["segment_id"] == row["segment_id"]
        ),
        None,
    )
    if matched_row is not None:
        label = _format_evidence_label(case_id, matched_row)
    else:
        label = f"{CASE_LABELS[case_id]} · {_friendly_role_label(row['role_label'])} · participant contribution"
    return (row["segment_text"].strip(), label)


def _question_text_fit(text: str, question_id: str) -> bool:
    return _question_signal_count(text, question_id) >= 2


def _question_signal_count(text: str, question_id: str) -> int:
    lowered = text.lower()
    return sum(1 for signal in QUESTION_TEXT_SIGNALS[question_id] if signal.lower() in lowered)


def _excerpt_sort_key(
    row: dict[str, str],
    top_code_set: set[str],
    evidence_score: dict[str, int],
) -> tuple[int, int, int]:
    relevance_score = _excerpt_relevance_score(row, top_code_set)
    return (
        relevance_score,
        evidence_score.get(row["evidence_type"], 0),
        -abs(len(row["excerpt_text"].strip()) - 220),
    )


def _excerpt_relevance_score(row: dict[str, str], top_code_set: set[str]) -> int:
    row_codes = {code for code in row["codes"].split(";") if code}
    direct_overlap = len(top_code_set.intersection(row_codes))
    if direct_overlap:
        return direct_overlap + 2
    concept_overlap = len(row_codes.intersection({
        "balance_multidimensional",
        "contentment_acceptance",
        "contentment_as_core",
        "spiritual_moral_anchor",
        "support_as_wellbeing_core",
        "family_support_ecology",
        "inner_peace_stability",
        "dignity_autonomy",
        "functionality_self_management",
        "professional_identity",
        "child_vulnerability",
        "practical_suggestion",
        "practical_recommendation",
        "healthcare_system_critique",
        "consultation_time_pressure",
        "access_delay_waiting",
        "communication_training_need",
        "patient_provider_relationship",
        "trust_questioning_barrier",
    }))
    return concept_overlap


def _oxford_join(items: list[str]) -> str:
    cleaned = [item for item in items if item]
    if not cleaned:
        return ""
    if len(cleaned) == 1:
        return cleaned[0]
    if len(cleaned) == 2:
        return f"{cleaned[0]} and {cleaned[1]}"
    return f"{', '.join(cleaned[:-1])}, and {cleaned[-1]}"


def _cross_day_profile(case_packages: dict[str, dict[str, Any]], question_id: str) -> list[str]:
    lines: list[str] = []
    for case_id, label in CASE_LABELS.items():
        question_row = next(row for row in case_packages[case_id]["question_evidence"] if row["question_id"] == question_id)
        excerpt_count = len(
            _unique_excerpt_rows(
                [row for row in case_packages[case_id]["excerpt_bank"] if row["question_id"] == question_id]
            )
        )
        lines.append(
            f"- **{label}**: `{question_row['participant_segments']}` participant segments; `{question_row['unique_participant_speakers']}` speakers; `{excerpt_count}` supporting quotations; main analytic patterns = `{_format_top_codes(question_row['top_codes'])}`"
        )
    return lines


def _cross_day_patterns(
    case_packages: dict[str, dict[str, Any]],
    matrix_rows: list[dict[str, str]],
    question_id: str,
) -> list[str]:
    matrix = next(row for row in matrix_rows if row["question_id"] == question_id)
    theme_values = {
        "IT1": int(matrix["IT1_segments"]),
        "IT2": int(matrix["IT2_segments"]),
        "IT3": int(matrix["IT3_segments"]),
        "IT4": int(matrix["IT4_segments"]),
    }
    ordered_themes = ", ".join(THEME_LABELS[key] for key, _ in sorted(theme_values.items(), key=lambda item: item[1], reverse=True))
    all_codes: list[str] = []
    evidence_types: Counter[str] = Counter()
    for case_id in CASE_LABELS:
        question_row = next(row for row in case_packages[case_id]["question_evidence"] if row["question_id"] == question_id)
        all_codes.extend(item for item in question_row["top_codes"].split(";") if item and item != "general_response")
        for row in _unique_excerpt_rows(case_packages[case_id]["excerpt_bank"]):
            if row["question_id"] == question_id:
                evidence_types[row["evidence_type"]] += 1
    most_common_codes = ", ".join(CODE_LABELS.get(code, code) for code, _ in Counter(all_codes).most_common(5))
    return [
        "",
        "###### Cross-day patterning",
        f"- **Integrated theme ordering for this question**: `{ordered_themes}`",
        f"- **Most repeated analytic patterns across the four workshops**: {most_common_codes}",
        f"- **Evidence mix for this question**: `{_format_evidence_mix(evidence_types)}` across the combined excerpts for this question",
    ]


def _unique_excerpt_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    unique_rows: list[dict[str, str]] = []
    seen_ids: set[str] = set()
    for row in rows:
        evidence_id = row["evidence_id"]
        if evidence_id in seen_ids:
            continue
        seen_ids.add(evidence_id)
        unique_rows.append(row)
    return unique_rows


def _table(rows: list[tuple[str, str, str]], headers: list[str]) -> list[str]:
    header = "| " + " | ".join(headers) + " |"
    divider = "| " + " | ".join(["---"] * len(headers)) + " |"
    body = ["| " + " | ".join(row) + " |" for row in rows]
    return [header, divider, *body]
