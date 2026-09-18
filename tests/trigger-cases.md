# Trigger Checks

These are manual smoke tests for the skill description and routing. A reviewer should confirm the first three activate this skill and the last two do not.

## Should trigger

1. “帮我做一款厨房收纳架的外观专利检索、保护范围分析和设计规避。”
2. “Check whether this physical product is visually close to the cited design patents and prepare supplier questions.”
3. “把这个汽车配件的外观风险拆成实质侵权、平台投诉、权属和未公开申请风险，并给三套改款方向。”

## Should not trigger

1. “请只做这个行业的市场规模和竞品价格分析。”
2. “帮我做一个实用专利权利要求 chart，不涉及产品外观。”

## Expected routing

The skill should activate for physical-product design-rights pre-screening and design-around planning. It should route pure market research, utility-patent claim analysis, and unrelated visual-design requests to other skills.
