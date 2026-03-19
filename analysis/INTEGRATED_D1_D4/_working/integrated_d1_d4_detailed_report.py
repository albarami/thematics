from __future__ import annotations


def build_detailed_life_course_report(
    question_totals: list[dict[str, str]],
    matrix_rows: list[dict[str, str]],
) -> str:
    """Build the detailed question-by-question integrated life-course report.

    Args:
        question_totals: Cross-case question total rows from the integrated summary layer.
        matrix_rows: Cross-case integrated question-by-theme matrix rows.

    Returns:
        The complete detailed integrated markdown report.
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
        "This report synthesizes the approved outward-facing packages for four life-course focus group workshops: Childhood (`CASE_D1`), Youth (`CASE_D2`), Adults (`CASE_D3`), and Elderly (`CASE_D4`). It is organized around the moderators’ seven discussion questions rather than around the cases alone, so that each question shows what was said in each life stage and what the cross-day pattern becomes when the four days are read together.",
        "",
        f"Across the integrated question layer, the report synthesizes `{total_segments}` participant segments drawn from the approved outward-facing reporting infrastructure. The strongest conceptual density sits in `Q3`, where the corpus most clearly explains how the five pillars are expected to improve wellbeing, while the strongest system-pressure density sits in `Q4` and `Q5`, where all four days describe care as only partially able to sustain the whole-person ideal they articulate earlier.",
        "",
        "The HT framework document positions `الحياة الطيبة` as a holistic, value-grounded life model organized through five interrelated pillars: spiritual, emotional, intellectual, physical, and social. Read through that lens, the overall picture across the four workshops is consistent: wellbeing is treated as multidimensional, morally and relationally grounded, and larger than symptom control. What changes across childhood, youth, adulthood, and older age is the social ecology that carries wellbeing, the kind of strain that threatens it, and the kind of redesign participants think would make healthcare more equal to it.",
        "",
        "## Methodology",
        "This synthesis uses only the approved outward-facing D1-D4 package layer. It draws on the final case reports, excerpt banks, question-theme matrices, summary tables, prominence tables, participant outputs, and the integrated D1-D4 synthesis materials. Raw transcripts, internal identity files, and non-approved case materials were not reopened for this report.",
        "",
        "Because the outward-facing case packages preserve evidence-type distinctions, the integrated report retains them. Verbatim transcript quotations remain the strongest quotation layer. Where a case package explicitly uses note-style transcript summary, note-taker summary, close-reading support, or auxiliary workbook material, this report keeps that status visible rather than rewriting it as uniform verbatim speech. Arabic remains authoritative where Arabic is the source language, while English quotations are preserved where they appear in the outward-facing case packages.",
        "",
        "The case-day reports were originally written before this workflow had the HT framework PDF in view. This integrated report therefore re-reads the outward-facing case findings through the HT framework lens without altering the underlying evidence base. The framework is used here to clarify what each day is emphasizing inside the five-pillar model, not to force the cases into a flat template or to invent new claims beyond the approved case packages.",
        "",
        "## HT framework orientation for this report",
        "- **Framework definition**: `الحياة الطيبة` is treated as an integrated form of flourishing across the spiritual, emotional, intellectual, physical, and social pillars.",
        "- **Interdependence rule**: The pillars are read as mutually shaping one another rather than as independent checklist items.",
        "- **Value clusters from the framework**: The PDF aligns the pillars with clusters such as care/cooperation/responsibility, health/strength/prevention, truth/wisdom/reflection, balance/determination/emotional refinement, and spiritual cultivation.",
        "- **Interpretive rule**: The integrated report tracks how the same HT framework is weighted differently across childhood, youth, adulthood, and older age rather than assuming identical emphasis in every case.",
        "",
        "## How theme weights were assigned",
        "- **Frequency**: How often a pattern recurred across the approved outward-facing question analyses, matrices, and excerpt-bank evidence.",
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
        "## Part One: Core Meaning & Experience",
        "",
    ]
    lines.extend(_render_q1(question_totals, matrix_rows))
    lines.extend(_render_q2(question_totals, matrix_rows))
    lines.extend(_render_q3(question_totals, matrix_rows))
    lines.extend(_render_q4(question_totals, matrix_rows))
    lines.extend([
        "## Part Two: Implementation (Challenges, Opportunities, Practical Suggestions)",
        "",
    ])
    lines.extend(_render_q5(question_totals, matrix_rows))
    lines.extend(_render_q6(question_totals, matrix_rows))
    lines.extend(_render_q7(question_totals, matrix_rows))
    lines.extend(
        [
            "## Consolidated Cross-Day Theme Dashboard",
            "- **The five-pillar HT model is the stable conceptual core**: Across all four days, `الحياة الطيبة` is read as multidimensional balance across spiritual, emotional, intellectual, physical, and social life rather than as simple symptom absence.",
            "- **Surface stability is an unreliable indicator**: Youth, adults, and elderly discussions all warn that calm appearance or visible functioning can conceal distress, burden, or unmet need; the childhood case raises the same caution through the theme of hidden distress and unreliable appearances.",
            "- **The social ecology changes across the life course**: Childhood is framed through professional-family support ecologies, youth through peer and disclosure worlds, adulthood through role-bearing strain, and older age through dignity, non-burden, and social recognition.",
            "- **Current services remain partial and uneven**: The strongest integrated service-facing pattern is that healthcare still over-concentrates on the physical pillar while relational, communicative, social, spiritual, and wider whole-person dimensions are inconsistently embedded.",
            "- **Fragmentation and time pressure are cross-day barriers**: Short encounters, weak continuity, hierarchy, explanation gaps, and uneven navigation recur in every day, though they are experienced differently at each life stage.",
            "- **Redesign logic is institutionally focused rather than purely interpersonal**: Participants repeatedly ask for embedded standards, training, communication reform, earlier prevention, stronger community linkage, and service models that do not rely on individual goodwill alone.",
            "",
            "## Final Policy-Ready Implications",
            "1. Adopt a holistic wellbeing framework as a service standard rather than treating it as an optional or informal add-on.",
            "2. Redesign care pathways so that physical, mental, social, family, and community supports can be coordinated rather than left fragmented across separate encounters.",
            "3. Protect the relational conditions of care by addressing time pressure, explanation quality, continuity, and the patient’s safety to disclose sensitive distress.",
            "4. Build prevention and early-intervention partnerships across life stages, especially through schools, families, community settings, and publicly understandable awareness structures.",
            "5. Treat workforce support, communication training, and culturally grounded practice as quality-of-care issues rather than optional professional extras.",
            "6. Embed dignity-sensitive, life-stage-responsive care standards so that childhood, youth, adulthood, and older age are not folded into one generic model of need.",
            "",
            "## Limits retained in this integrated report",
            "This report inherits the limits of the approved case packages rather than dissolving them by aggregation. These include the Day 1 late-question coding gap and auxiliary-only Q7 layer, the note-style and note-supported caution in parts of Day 2, the attribution and late-question preservation limits in Day 3, and the granularity, merged-late-section, and contribution-concentration cautions in Day 4.",
            "",
        ]
    )
    return "\n".join(lines)


def _render_q1(question_totals: list[dict[str, str]], matrix_rows: list[dict[str, str]]) -> list[str]:
    return [
        "### Q1. What is wellbeing for you?",
        "ما معنى الحياة الطيبة بالنسبة لك؟",
        "",
        _question_profile(question_totals, matrix_rows, "Q1"),
        "Across the four life stages, wellbeing is introduced as an inner, relational, and value-governed condition before it is ever discussed as a service outcome. Read through the HT lens, `Q1` establishes `الحياة الطيبة` as integrated flourishing across the spiritual, emotional, intellectual, physical, and social pillars, with each day weighting those pillars differently. The integrated evidence for `Q1` is led by the multidimensional-balance theme, and the opening discussion across all four days establishes the moral and interpretive standard against which later healthcare realities are judged.",
        "",
        "#### Detailed findings by life stage",
        "##### Childhood",
        "The Day 1 childhood case defines wellbeing through `قناعة` (contentment), `توازن` (balance), and spiritual grounding. Read through the HT framework, childhood wellbeing is not introduced as a technical child-development score; it is framed as a morally anchored good life whose spiritual, emotional, social, physical, and intellectual parts must hold together. Because the cleanest Day 1 evidence comes mainly from professionals, this opening definition also shows the case’s provider-led perspective: children’s wellbeing is described through adult interpretive stewardship rather than through sustained child voice.",
        "",
        "##### Youth",
        "The Day 2 youth case keeps the balance language but adds stronger emphasis on usefulness, self-regard, and social-moral positioning. Youth wellbeing is described as being satisfied with oneself, useful to self and others, and held in a workable relational environment. The result is a youth-specific version of balance that is still morally grounded but already more exposed to identity, peer life, and the challenge of staying psychologically steady while socially visible.",
        "",
        "##### Adults",
        "The Day 3 adult case shifts the emphasis from abstract peace to livable coping under pressure. Adult wellbeing is defined through contentment, relational positioning, balance, and the practical ability to keep going despite stressors. This makes Day 3 conceptually broad but already burden-sensitive: adults are well not because life is easy, but because they can sustain inner steadiness without collapsing under accumulated responsibilities.",
        "",
        "##### Elderly",
        "The Day 4 elderly case adds the strongest dignity language. Older-age wellbeing is described through peace, faith, contentment, containment, and the refusal to reduce an older person to burden or decline. The elderly case therefore keeps the multidimensional logic of the earlier days but gives special weight to social standing, acceptance, and being held with dignity rather than merely managed clinically.",
        "",
        "#### Key themes",
        *_table(
            [
                ("Inner contentment and peace", "Wellbeing is repeatedly described as calm, satisfaction, acceptance, and inner steadiness across all four days.", "Primary"),
                ("Multidimensional balance", "Physical, emotional, social, spiritual, and intellectual life are treated as interdependent rather than separable.", "Primary"),
                ("Values and spiritual grounding", "Faith, moral orientation, and culturally grounded meanings stabilize how the good life is understood.", "Primary"),
                ("Relational usefulness and contribution", "Being useful, held, socially connected, or valuable to others remains part of wellbeing, especially in youth and adulthood.", "Secondary"),
                ("Dignity and social standing", "Older-age and adult discussion add the importance of personhood, respect, and non-reduction to burden.", "Secondary"),
            ],
            ["Theme", "Summary", "Weight"],
        ),
        "",
        "#### Illustrative quotes",
        '- **Childhood**: "My wellbeing is a sense of being content, not happy or sad, just content." `[note-taker record, HWCH0NT1, Table 0]`',
        '- **Youth**: "الحياة طيبة يعني كما تفضل الإخوة الكرام الأعزاء تعني الرضا، هل أنت راضي عن ذاتك؟ تعني أن تكون مفيدا لنفسك ولغيرك." `[HWYO0AR, Table 0, verbatim transcript, D2_S0011]`',
        '- **Adults**: "To me, well-being is really all about feeling reasonably content and able to cope with the stressors... despite all of that, having the happy Tuesdays and the happy Wednesdays, that is well-being for me." `[HWAD10AR, Table 10, coded transcript support, D3_S0004]`',
        '- **Elderly**: "For me, well-being is the integration of all aspects: spiritual, emotional, physical, and mental. It means living peacefully and being satisfied with whatever comes to you, even if you have a disability." `[HWEL10AR, Table 10, coded transcript support, D4_S0009]`',
        "",
        "#### Cross-day conclusion",
        "Taken together, `Q1` shows that the life-course workshops do not begin from illness, service gaps, or narrow definitions of health. They begin from a value-laden concept of the good life. Across all four days, wellbeing means multidimensional balance, but the social and moral weighting of that balance changes by life stage: safety and spiritual steadiness in childhood, workable identity and usefulness in youth, coping under role pressure in adulthood, and dignity-preserving balance in older age.",
        "",
    ]


def _render_q2(question_totals: list[dict[str, str]], matrix_rows: list[dict[str, str]]) -> list[str]:
    return [
        "### Q2. When we describe someone as ‘well,’ what do we mean?",
        "كيف تعرف العافية؟",
        "",
        _question_profile(question_totals, matrix_rows, "Q2"),
        "Across the integrated corpus, `Q2` makes explicit that wellness is not equivalent to having no disease. Read through the HT framework, this question asks whether the five-pillar model is actually visible in a person’s lived functioning rather than only in abstract definition. Participants repeatedly define being ‘well’ through wider functioning, emotional steadiness, contextual fit, and the need to look beyond visible appearance. This question narrows the conceptual frame of `Q1` into a more diagnostic and interpretive test of what real wellness looks like.",
        "",
        "#### Detailed findings by life stage",
        "##### Childhood",
        "The Day 1 childhood case uses `Q2` to distinguish broad wellbeing from the more concrete condition of `عافية` or being well. Participants accept the five pillars as a useful language of integration, but they also signal that the framework is not always intuitive in practice. This matters because Day 1 wellness is not a checklist outcome; it is an observed balance that still depends on interpretation and context.",
        "",
        "##### Youth",
        "In Day 2, youth wellness is strongly tied to functioning: getting up, participating, remaining productive, feeling psychologically settled, and maintaining social relationships. But the youth case also shows why this is not enough. Because functioning is used as part of the definition, the case simultaneously prepares the warning that outward functionality can hide distress, especially where disclosure is difficult or shame-sensitive.",
        "",
        "##### Adults",
        "The adult case adds responsibility and value orientation. Adults are described as well when they can appreciate where they are, maintain their responsibilities, and sustain themselves across competing obligations. Day 3 therefore defines wellness in a way that is broader than visible performance but still shaped by what adulthood expects a person to carry.",
        "",
        "##### Elderly",
        "The elderly case pushes the question further by warning that calm appearance may be profoundly misleading. Older people may hide distress because they do not want to become a burden, so being well requires a wider, 360-degree inquiry into social, emotional, spiritual, and environmental conditions. Day 4 makes independence and functional ability important, but only as part of a larger, deeper account of older-age wellness.",
        "",
        "#### Key themes",
        *_table(
            [
                ("Holistic functioning", "Wellness requires inquiry into family, work, relationships, health, and context rather than only disease status.", "Primary"),
                ("Psychological steadiness", "Peace of mind, emotional balance, and inner regulation are central to describing someone as well.", "Primary"),
                ("Hidden distress beneath appearance", "Surface calm, functionality, or compliance may conceal anxiety, depression, burnout, or non-burden behaviour.", "Secondary"),
                ("Independence and functional ability", "Especially salient in the elderly case, but present more broadly as part of meaningful participation in daily life.", "Secondary"),
                ("Role-fit and responsibility", "Adult and youth discussions link wellness to the ability to keep life functioning without taking visible appearance at face value.", "Secondary"),
            ],
            ["Theme", "Summary", "Weight"],
        ),
        "",
        "#### Illustrative quotes",
        '- **Childhood**: "حالة تكاملية من التوازن بين جميع الركائز (الروحية / الجسدية / الاجتماعية / العاطفية / الفكرية)" `[note-taker summary, HWCH6NT3, Table 6]`',
        '- **Youth**: "For me, I think it\'s about functioning again, right? So if you are able to get up in the morning and do everything that you need to do..." `[HWYO9AR, Table 9, verbatim transcript, D2_S0255]`',
        '- **Adults**: "I think it\'s about appreciating where you are at and doing whatever you can... And I think that\'s an adult\'s responsibility." `[HWAD10AR, Table 10, coded transcript support, D3_S0067]`',
        '- **Elderly**: "It is all integrated... Elderly people often hide their problems because they don\'t want to be a burden, so you have to look deeper than just physical symptoms." `[HWEL10AR, Table 10, coded transcript support, D4_S0013]`',
        "",
        "#### Cross-day conclusion",
        "`Q2` shows the strongest shared rejection of biomedical minimalism. Across childhood, youth, adulthood, and older age, being well means more than being disease-free. It means being held together psychologically, socially, spiritually, and functionally. Just as importantly, the workshops agree that outward appearance is an unreliable guide: a child may look settled, a young person may keep functioning, an adult may keep performing roles, and an older person may avoid burdening others, while distress remains hidden underneath.",
        "",
    ]


def _render_q3(question_totals: list[dict[str, str]], matrix_rows: list[dict[str, str]]) -> list[str]:
    return [
        "### Q3. How can the five HT pillars improve your wellbeing?",
        "كيف تسهم الركائز الخمسة في تحسين عافيتك؟",
        "",
        _question_profile(question_totals, matrix_rows, "Q3"),
        "`Q3` is the most evidence-rich question in the integrated corpus. It is where the workshops move most clearly from defining wellbeing into explaining how it is strengthened. The HT framework document itself positions the five pillars as interrelated and value-bearing rather than as flat technical domains, and the workshop evidence strongly confirms that logic. Across all four life stages, the pillars are not treated as isolated domains. They are described as mutually reinforcing, with the meaning and weighting of that reinforcement changing across the life course.",
        "",
        "#### Detailed findings by life stage",
        "##### Childhood",
        "The Day 1 childhood case treats `Q3` as the bridge between concept and practice. Participants explain how spiritual and emotional grounding support the other pillars, then move into the ecology through which children might actually experience that support: schools, clinics, families, communities, and early-awareness structures. Day 1 therefore makes the pillars actionable through childhood support systems rather than by describing them as purely personal traits.",
        "",
        "##### Youth",
        "The youth case gives the strongest relational reading of the pillars. Participants describe young people as living through families, peers, schools, and digital environments, and they repeatedly elevate the social pillar because youth wellbeing is rarely sustainable in isolation. The youth contribution to `Q3` is therefore that the pillars matter not only because they are individually desirable, but because they shape how social disconnection or support is lived.",
        "",
        "##### Adults",
        "The adult case brings in a tension that is especially important for the integrated report: the pillars require self-work, but they cannot be enacted through self-discipline alone. Adults speak about responsibility toward self, children, family, and wider life, but they also insist that systems cannot be ignored. Day 3 is therefore the clearest site where the pillar discussion resists collapsing into individual blame.",
        "",
        "##### Elderly",
        "The elderly case argues most strongly that the pillars are weighted rather than flat. Participants do not deny that all five pillars matter, but they repeatedly show that dignity, social significance, spiritual steadiness, and continued usefulness become especially heavy in older age. Day 4 therefore uses `Q3` to challenge reductive age narratives and to insist that improving wellbeing also requires rethinking what ageing itself is taken to mean.",
        "",
        "#### Key themes",
        *_table(
            [
                ("Interconnected pillars", "The five pillars are treated as a system in which strengthening one domain often supports the others.", "Primary"),
                ("Spiritual coping and protection", "Faith, moral orientation, and spiritual grounding are repeatedly described as stabilizing responses to stress and uncertainty.", "Primary"),
                ("Social support as resilience", "Family, peers, schools, community, and social recognition are treated as essential resilience structures.", "Primary"),
                ("System responsibility for pillar enactment", "Participants insist that people cannot simply carry the pillars alone if institutions remain unchanged.", "Secondary"),
                ("Life-stage weighting of the pillars", "Older age especially shows that the pillars are not experienced as flat or equal in practice.", "Secondary"),
            ],
            ["Theme", "Summary", "Weight"],
        ),
        "",
        "#### Illustrative quotes",
        '- **Childhood**: "Short term and long term. The long term. Definitely is implementing it in the teaching system from the get go elementary up..." `[HWCH0AR, Table 0, verbatim transcript, Day 1 Q3 report quotation]`',
        '- **Youth**: "العزلة في مفهومنا الحديث لا تعني غياب العائلة أو الوالدين، بل تعني أن يعيش الفرد داخل أسرته ومع ذلك يظل معزولاً." `[HWYO0AR, Table 0, verbatim transcript, D2_S0028]`',
        '- **Adults**: "Yes, we should think individual, but we should think systems... نهمل الsystems." `[HWAD3AR, Table 3, coded transcript support from an unclear row, D3_S0562]`',
        '- **Elderly**: "برأيي إنه إحنا محتاجين نعيد تعريف مين هم كبار السن... هدول مفيدين." `[HWEL3AR, Table 3, coded transcript support, D4_S0068]`',
        "",
        "#### Cross-day conclusion",
        "Across D1-D4, `Q3` shows that the five pillars are useful precisely because participants do not treat them as a flat checklist. The pillars improve wellbeing when they operate together, when they are carried by supportive relationships and institutions, and when their weighting matches life stage. Childhood and youth stress ecology and early support, adulthood stresses the balance between self and system responsibility, and older age stresses dignity, usefulness, and socially meaningful ageing.",
        "",
    ]


def _render_q4(question_totals: list[dict[str, str]], matrix_rows: list[dict[str, str]]) -> list[str]:
    return [
        "### Q4. Are HT pillars reflected in current healthcare services?",
        "هل تنعكس الركائز في خدمات الرعاية الصحية حاليا؟",
        "",
        _question_profile(question_totals, matrix_rows, "Q4"),
        "`Q4` is the clearest turning point from ideal to service reality. Across all four days, participants do not usually claim that the pillars are completely absent. Instead, they describe healthcare as only partially reflecting them: strongest on the physical pillar, uneven on emotional and social support, and inconsistent in how spiritual meaning, communication, culture, and wider life context are integrated. Read through the HT framework lens, `Q4` is the first sustained test of whether the five-pillar model has actually been embedded in service delivery rather than only endorsed in principle.",
        "",
        "#### Detailed findings by life stage",
        "##### Childhood",
        "In the childhood case, `Q4` opens the sharp gap between the earlier moral-spiritual ideal and real childhood service conditions. Participants describe fragmented encounters, weak follow-up, narrow problem-handling, and poor coordination across systems that should support children more coherently. The result is not a denial that good practice exists, but an insistence that children encounter an uneven service ecology rather than a stable whole-person pathway.",
        "",
        "##### Youth",
        "The youth case adds explicit pressure language. Participants say that empathy, relational support, and broader wellbeing often fall out of care once waiting rooms, throughput pressure, and crisis-driven models dominate the encounter. Day 2 therefore frames current services as capable of isolated whole-person gestures, but still structurally tilted toward illness response over youth wellbeing and prevention.",
        "",
        "##### Adults",
        "The adult case describes the pillars as partially visible but weakly integrated. Adults can receive strong physical treatment, but participants ask what happens once the encounter ends: how living, coping, explaining, and navigating are actually sustained. Delayed appointments, uneven explanation, and the difficulty of making care feel whole-person rather than episodic are central to the Day 3 reading of `Q4`.",
        "",
        "##### Elderly",
        "The elderly case is especially explicit that the problem is uneven institutionalization. Participants say that some providers or services do reflect the pillars, but only in an ad hoc or locally dependent way rather than as a system-wide expectation. Older-age care is therefore described as patchily holistic: there are pockets of elder-sensitive practice, but not a consistently embedded model across the wider system.",
        "",
        "#### Key themes",
        *_table(
            [
                ("Biomedical dominance", "Physical care remains the strongest and most stable element of current services, while wider pillars are less consistently held.", "Primary"),
                ("Fragmentation and short encounter time", "Siloed pathways, rushed encounters, and weak follow-up limit holistic assessment and continuity.", "Primary"),
                ("Partial rather than full institutional embedding", "Good practice exists, but it often depends on particular providers, tables, or services rather than uniform standards.", "Primary"),
                ("Relational, cultural, and spiritual gaps", "Empathy, disclosure safety, cultural fit, and spiritual meaning are unevenly integrated across current care.", "Secondary"),
                ("Variation by institution and setting", "Participants repeatedly describe pockets of strength rather than a single consistent system model.", "Secondary"),
            ],
            ["Theme", "Summary", "Weight"],
        ),
        "",
        "#### Illustrative quotes",
        '- **Childhood**: "Speaking as a service receiver, she criticized the one-problem rule in 10-minute consultations, which forces patients to see multiple practitioners to get their holistic needs met." `[HWCH10AR, Table 10, note-style summary, Day 1 Q4 report quotation]`',
        '- **Youth**: "The pressure of having 30 patients waiting outside damages the image of healthcare professionals because they cannot spend enough time with each person." `[HWYO10AR, Table 10, note-style transcript summary, D2_S0089]`',
        '- **Adults**: "They said to us, the physicians or the medical team helps us get physically better... But when we leave the facility, how are we living? How is our well-being?" `[HWAD10AR, Table 10, coded transcript support, D3_S0225]`',
        '- **Elderly**: "ولكن قد تعتمد... على مقدم الخدمة الطبية... ولكن ليس بطريقة مؤسساتية ابدا." `[HWEL7AR, Table 7, coded transcript support, D4_S0173]`',
        "",
        "#### Cross-day conclusion",
        "The cross-day conclusion for `Q4` is that the pillars are visible, but not yet reliably built into care. Childhood shows the problem as fragmented child-service ecology, youth as pressure and prevention failure, adulthood as uneven explanation and navigability, and older age as patchy institutionalization. The common pattern is not total absence; it is partial reflection under conditions that still over-weight physical care and under-support the whole-person frame established earlier in the workshops.",
        "",
    ]


def _render_q5(question_totals: list[dict[str, str]], matrix_rows: list[dict[str, str]]) -> list[str]:
    return [
        "### Q5. Main challenges integrating HT pillars into healthcare — and what makes it possible or not possible?",
        "ما التحديات الرئيسية التي تواجه الدمج؟ وما الذي يجعل الدمج ممكنًا أو غير ممكن؟",
        "",
        _question_profile(question_totals, matrix_rows, "Q5"),
        "`Q5` concentrates the barrier layer across the integrated corpus. The strongest cross-day pattern is that whole-person care is blocked less by abstract disagreement than by operational culture: time pressure, weak continuity, hierarchy, communication gaps, fragmented pathways, and service environments that make disclosure, explanation, and dignity harder to sustain in real time.",
        "",
        "#### Detailed findings by life stage",
        "##### Childhood",
        "In the childhood case, the challenge layer focuses on listening, coordination, and participatory decision-making. Participants do not say that professionals lack concern; they say the surrounding structures make good listening, inclusion, and joined-up action hard to sustain. Day 1 therefore frames childhood barriers as system failures around children rather than as isolated deficits within any one practitioner.",
        "",
        "##### Youth",
        "The youth case sharpens the trust and disclosure problem. Participants describe privacy concerns, stigma, and the tendency for distress to be expressed through bodily complaint when direct disclosure feels unsafe. The challenge in Day 2 is not only time pressure; it is the difficulty of building care encounters where young people can speak safely enough for whole-person wellbeing to become visible.",
        "",
        "##### Adults",
        "The adult case highlights rights awareness, the difficulty of questioning providers, hierarchy-sensitive communication, and the failure to explain complex care in ways adults can actually use. Day 3 therefore treats integration barriers as both structural and relational: adults need navigable systems, but they also need encounters in which asking questions and understanding options do not feel like challenges to authority.",
        "",
        "##### Elderly",
        "The elderly case combines time scarcity, staffing pressure, language mismatch, and the translational difficulty of turning dignity, inclusion, and social recognition into repeatable care practice. Day 4’s barrier layer is especially useful because it shows that even when providers endorse the values, they still struggle to operationalize them under pressured, unequal conditions.",
        "",
        "#### Key themes",
        *_table(
            [
                ("Time pressure and encounter compression", "Short appointments and overloaded care environments reduce the space for listening, exploration, explanation, and relational safety.", "Primary"),
                ("Fragmented and siloed pathways", "Patients and families move across services without stable integration, continuity, or shared care logic.", "Primary"),
                ("Hierarchy, translation, and communication barriers", "Patients may not receive clear explanation, may hesitate to question clinicians, or may struggle across language and cultural mismatches.", "Primary"),
                ("Stigma, trust, and disclosure difficulty", "Especially visible in youth and adulthood, but relevant across the life course wherever distress is hidden or socially costly to reveal.", "Secondary"),
                ("Workforce and implementation strain", "Even well-intentioned providers may not be supported enough to consistently deliver the pillar-based model they endorse.", "Secondary"),
            ],
            ["Theme", "Summary", "Weight"],
        ),
        "",
        "#### Illustrative quotes",
        '- **Childhood**: "You said remember, enjoy the six weeks you doing psychiatry... the root of everything is somebody taking the time to listen..." `[HWCH0AR, Table 0, verbatim transcript, Day 1 Q5 report quotation]`',
        '- **Youth**: "فعندما تُفصح المريضة للطبيبة عن معاناتها مع الاكتئاب، فإنها تمنحها ثقتها بناءً على موافقة ضمنية بأن تظل هذه المعلومة سرية" `[HWYO0AR, Table 0, verbatim transcript, D2_S0046]`',
        '- **Adults**: "You\'re challenging my authority or you\'re challenging my decision. I\'ve had situations... in which I\'ve gone to an appointment and I have asked questions of the provider." `[HWAD10AR, Table 10, coded transcript support, D3_S0338]`',
        '- **Elderly**: "The biggest challenges are staffing and time. Consultations are often less than 10 minutes, making it hard to explore a person\'s whole life. Language barriers are also an issue." `[HWEL10AR, Table 10, coded transcript support, D4_S0021]`',
        "",
        "#### What makes integration more possible",
        "- **Leadership plus frontline readiness**: The cases repeatedly imply that values alone are insufficient unless institutions and practitioners meet in the middle.",
        "- **Interdisciplinary and cross-setting coordination**: Childhood and youth especially point to school-health-family linkage, while adult and elderly cases add broader service redesign and coordinated pathways.",
        "- **Shared language, rights, and communication standards**: Adults and elderly discussions repeatedly show that integration becomes more possible when patients understand care and can speak safely within it.",
        "- **Culturally grounded implementation**: Across all four days, participants do not ask for abstract universal frameworks alone; they ask for locally meaningful, culturally and spiritually responsive translation into practice.",
        "",
        "#### Cross-day conclusion",
        "The integrated reading of `Q5` is that the main barriers are systemic and operational before they are ideological. Participants across all life stages already understand the value of whole-person care. What blocks it is the way services are currently organized: compressed time, fragmented pathways, uneven explanation, weak relational safety, and limited institutional support for carrying the wider pillars into real care delivery. What makes integration more possible is therefore not motivational rhetoric alone, but redesign, coordination, communicative safety, and culturally grounded implementation.",
        "",
    ]


def _render_q6(question_totals: list[dict[str, str]], matrix_rows: list[dict[str, str]]) -> list[str]:
    return [
        "### Q6. What opportunities exist now to enhance integration?",
        "ما الفرص المتاحة حاليا لتعزيز الدمج؟",
        "",
        _question_profile(question_totals, matrix_rows, "Q6"),
        "`Q6` is where the workshops begin to identify openings already present in the current environment. The integrated evidence is smaller and more methodologically uneven than `Q3-Q5`, but it is still analytically important because it shows that participants are not speaking only in abstract aspirations. They can point to concrete entry points that already exist and could be strengthened.",
        "",
        "#### Detailed findings by life stage",
        "##### Childhood",
        "The childhood case identifies schools as the strongest existing opportunity structure. Participants repeatedly describe school-based awareness and early education as the most realistic route for reaching children before needs deepen. Day 1 also implies that broader community awareness and workforce support remain important, but the outward-facing evidence layer is underindexed in `Q6`, so the strongest reportable opportunity claim remains the school setting itself.",
        "",
        "##### Youth",
        "The youth case makes the opportunity layer highly practical. Participants point to school nurses, parent education, and earlier assessment structures as existing but underused resources. Day 2 therefore treats opportunity not as a blank future state but as latent infrastructure: settings and roles already exist, but they need stronger training, clearer purpose, and a more youth-sensitive design.",
        "",
        "##### Adults",
        "The adult case identifies accessible counseling and awareness structures as the clearest current openings. Free counseling provision, stronger public campaigns, and cross-sector linkage appear as viable routes that already exist in partial form. But Day 3 also carries an explicit caution: late-question preservation is uneven, so the opportunity layer is real without being equally clean across every source.",
        "",
        "##### Elderly",
        "The elderly case combines service accessibility with public preparation. Participants identify home care, awareness campaigns, and technology-enabled support as real opportunity structures, but they insist these tools must be introduced carefully and without reducing older people to passive recipients. Day 4 therefore treats opportunity as something that can extend access and inclusion, but only if it remains elder-sensitive and appropriately timed.",
        "",
        "#### Opportunity themes",
        *_table(
            [
                ("School, family, and community partnerships", "Existing educational and community settings can carry earlier awareness, prevention, and support across childhood and youth.", "Primary"),
                ("Prevention and early awareness", "Participants repeatedly identify earlier, proactive framing as more effective than waiting for crisis or late presentation.", "Primary"),
                ("Accessible support entry points", "Free counseling, home care, frontline roles, and practical access routes are already present in partial form and can be strengthened.", "Primary"),
                ("Culturally meaningful framing", "Opportunities become stronger when wellbeing language is locally understandable and socially acceptable.", "Secondary"),
                ("Technology and outreach with caution", "Digital tools and home-linked services can extend care, but only when introduced with attention to fit, timing, and dignity.", "Secondary"),
            ],
            ["Opportunity", "What it enables", "Weight"],
        ),
        "",
        "#### Illustrative quotes",
        '- **Childhood**: "من المدارس. لو بدأنا من المدارس وبدأنا الوعي من المدارس..." `[HWCH2AR, Table 2, verbatim transcript, Day 1 Q6 report quotation]`',
        '- **Youth**: "School nurses should ideally be trained more than just somebody who wipes the kid\'s nose when they have a sniffle." `[HWYO9AR, Table 9, verbatim transcript, D2_S0304]`',
        '- **Adults**: "الفرصة الكبيرة التي نراها ما شاء الله عندنا موجودة هنا نحن في جامعة قطر نوفر psycho therapy counseling for free." `[HWAD4AR, Table 4, close-reading support, D3_S0863]`',
        '- **Elderly**: "Opportunity: She identifies bringing services directly to the patient through home care and proactively preparing the public through awareness campaigns as key opportunities." `[HWEL10AR, Table 10, coded transcript support, D4_S0024]`',
        "",
        "#### Cross-day conclusion",
        "The cross-day conclusion for `Q6` is that opportunity already exists, but it is scattered rather than fully integrated. Childhood and youth show the strength of school and family-linked entry points. Adulthood shows that free access points and public campaigns can already carry wellbeing work. Older age shows that home care, awareness, and careful technology use can widen reach. The consistent lesson is that opportunity is real, but it becomes transformative only when institutions strengthen and coordinate what is already available.",
        "",
    ]


def _render_q7(question_totals: list[dict[str, str]], matrix_rows: list[dict[str, str]]) -> list[str]:
    return [
        "### Q7. What practical suggestions do you have for integrating HT pillars to improve healthcare services?",
        "اقتراحات عملية لطرق الدمج؟",
        "",
        _question_profile(question_totals, matrix_rows, "Q7"),
        "`Q7` contains the most explicitly redesign-oriented part of the integrated corpus. Although the cross-day question layer is smaller and includes substantial attribution caution in some cases, the practical-suggestion material is still one of the clearest places where the four life stages converge: participants are not asking only for kinder attitudes. They are asking for redesign in service pathways, communication, training, dignity, quality standards, and institution-level embedding of the HT framework.",
        "",
        "#### Detailed findings by life stage",
        "##### Childhood",
        "The childhood case has the thinnest outward-facing `Q7` transcript layer. The final Day 1 package explicitly states that no outward-facing `Q7` excerpt-bank rows survive as transcript-equivalent quotation evidence, and that practical suggestions are therefore preserved mainly in the auxiliary recommendation workbook. Even with that limitation, the Day 1 practical layer remains clear: school-based awareness, workforce training, community wellness centers, parenting and family support, digital coordination, culturally adapted intervention frameworks, and extracurricular wellbeing activity.",
        "",
        "##### Youth",
        "The youth case turns practical suggestion into communication and trust design. Participants call for social-media awareness, safer private routes to support, and clearer youth-facing signals that school and healthcare services can be trusted without judgment. Day 2 therefore keeps the practical layer strongly linked to disclosure safety and institutional confidence-building rather than generic awareness alone.",
        "",
        "##### Adults",
        "The adult case moves most directly into system redesign. Participants focus on the time problem, integration of the five pillars into actual service organization, workforce training, and licensing-linked professional development. Even where the strongest late Day 3 lines are attribution-cautious, the practical direction is unmistakable: adult-care redesign requires institutions to carry the framework, not merely individual practitioners improvising it.",
        "",
        "##### Elderly",
        "The elderly case contains the strongest and broadest practical redesign logic. Participants propose communication training, elderly-specific clubs or social-health spaces, stronger institutional culture around the pillars, clearer rights and responsibilities, and licensing-linked training expectations. Day 4 therefore makes the practical layer highly concrete: redesign should be visible in physical access, social inclusion, professional development, and organization-wide norms.",
        "",
        "#### Priority recommendations",
        "##### Service design and pathways",
        "- Use more coordinated, team-based care pathways where physical, mental, social, and community supports do not remain isolated from one another.",
        "- Strengthen one-stop or better-coordinated access where life stage and complexity make multiple disconnected contacts especially burdensome, particularly for older adults and complex family situations.",
        "",
        "##### Quality standards and indicators",
        "- Complement throughput logic with wellbeing-sensitive indicators that capture relational quality, continuity, dignity, communication, and the wider five-pillar experience of care.",
        "- Treat HT framework integration as a measurable service standard rather than an informal aspiration left to local goodwill alone.",
        "",
        "##### Communication, dignity, and relational quality",
        "- Make communication training, explanation quality, and respectful relational practice visible service expectations rather than personal extras.",
        "- Build trust signals and disclosure-safe routes for youth and other groups who may hide distress when care feels exposing, judgmental, or socially risky.",
        "",
        "##### Workforce and professional development",
        "- Link pillar-based care more explicitly to staff development, ongoing training, and professional expectations so whole-person care is not left to ad hoc goodwill.",
        "- Treat the conditions that support listening, explanation, continuity, supervision, and staff recovery as quality-of-care issues, not optional soft skills.",
        "",
        "##### Prevention and community linkage",
        "- Strengthen school-health collaboration for early prevention, youth support, and family-linked awareness work.",
        "- Expand community and socially meaningful spaces that reduce isolation, especially in older age.",
        "",
        "##### Cultural and spiritual responsiveness",
        "- Preserve culturally grounded communication and, where appropriate and desired, spiritually meaningful support options without reducing care to a single moral formula.",
        "- Ensure implementation language is locally legible and life-stage responsive rather than copied in a flat way across all groups.",
        "",
        "#### Illustrative quotes",
        '- **Childhood**: No outward-facing transcript-equivalent `Q7` quote is preserved in the Day 1 package; the practical layer survives in the auxiliary workbook categories only. `[auxiliary workbook summary, Day 1 final report Appendix C]`',
        '- **Youth**: "I think maybe one other suggestion... we can do a social media campaign... and they can trust the services in the school, in the healthcare, to express themselves, and they will get help without being judged." `[HWYO9AR, Table 9, verbatim transcript, D2_S0313]`',
        '- **Adults**: "دمج الركائز الخمسة للحياة الطيبة بشكل متكامل في الخدمات الصحية... وإدماج الركائز الخمسة للحياة الطيبة ضمن تكوين وتدريب الكوادر الطبية والشبه الطبية... وتجديد التراخيص المهنية." `[HWAD6AR, Table 6, close-reading support from an unclear row, D3_S1153]`',
        '- **Elderly**: "Suggestion: Her suggestions focus on fundamental skills and clarity: mandating communication training for providers and having policymakers clearly define the rights and responsibilities of all parties to foster mutual respect." `[HWEL10AR, Table 10, coded transcript support, D4_S0028]`',
        '- **Elderly**: "يجب أن يكون عندك 40 CBD تدريب 40 CBD مؤتمرات وهذا يجب أن تكون لجل تجدد رخصة الحياة طيبة ضمن التطوير المهني للعاملين." `[HWEL9AR, Table 9, coded transcript support, D4_S0625]`',
        "",
        "#### Cross-day conclusion",
        "The cross-day conclusion for `Q7` is that practical integration means redesign. Childhood points to structured awareness and family/community supports, youth to trust-building and accessible communication channels, adulthood to training and system reorganization, and older age to institutional embedding, dignity-sensitive spaces, and professional development. The practical layer across D1-D4 therefore converges not on one program, but on a redesign logic: whole-person care becomes more real when institutions, pathways, communication, and community linkages are deliberately built around it.",
        "",
    ]


def _question_profile(
    question_totals: list[dict[str, str]],
    matrix_rows: list[dict[str, str]],
    question_id: str,
) -> str:
    totals = next(row for row in question_totals if row["question_id"] == question_id)
    dominant_themes = _dominant_themes(matrix_rows, question_id)
    dominant_text = ", ".join(dominant_themes[:-1]) + f" and {dominant_themes[-1]}" if len(dominant_themes) > 1 else dominant_themes[0]
    return (
        f"**Integrated evidence profile:** `{totals['participant_segments']}` participant segments, "
        f"`{totals['summed_unique_participant_speakers']}` summed participant-speaker counts, "
        f"dominant integrated theme(s): {dominant_text}."
    )


def _dominant_themes(matrix_rows: list[dict[str, str]], question_id: str) -> list[str]:
    row = next(item for item in matrix_rows if item["question_id"] == question_id)
    labels = {
        "IT1": "`IT1` multidimensional balance and moral grounding",
        "IT2": "`IT2` relational ecology across the life course",
        "IT3": "`IT3` partial and fragmented reflection in current care",
        "IT4": "`IT4` institutionally embedded redesign",
    }
    values = {
        "IT1": int(row["IT1_segments"]),
        "IT2": int(row["IT2_segments"]),
        "IT3": int(row["IT3_segments"]),
        "IT4": int(row["IT4_segments"]),
    }
    top_value = max(values.values())
    return [labels[key] for key, value in values.items() if value == top_value]


def _table(rows: list[tuple[str, str, str]], headers: list[str]) -> list[str]:
    header = "| " + " | ".join(headers) + " |"
    divider = "| " + " | ".join(["---"] * len(headers)) + " |"
    body = ["| " + " | ".join(row) + " |" for row in rows]
    return [header, divider, *body]
