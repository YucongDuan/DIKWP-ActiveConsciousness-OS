#!/usr/bin/env python3
"""Offline demo for DIKWP ActiveConsciousness OS.
No model API required. Generates a functional active-consciousness replay bundle.
"""
import json, re, datetime

def analyse_context(text):
    patterns=[]; tags=[]; risks=[]
    if re.search(r"总是|一直|反复|迟迟|经常|always|repeatedly", text, re.I): patterns.append('repeated_loop')
    if re.search(r"不敢|害怕|焦虑|担心|fear|anxiety", text, re.I): tags.append('fear_or_evaluation_pressure')
    if re.search(r"资料|收集|阅读|information|research", text, re.I): patterns.append('information_accumulation_without_collapse')
    if re.search(r"提交|发布|公开|发送|publish|submit", text, re.I): risks.append('public_commitment_irreversibility')
    if re.search(r"医疗|法律|投资|辞职|离婚|medical|legal|invest|divorce", text, re.I): risks.append('high_stakes_decision')
    return patterns,tags,risks

def build_replay(context, purpose, autonomy='A2'):
    patterns,tags,risks = analyse_context(context)
    high = 'high_stakes_decision' in risks
    info = 'Detected repeated loop and information accumulation without collapse.' if patterns else 'Detected open action loop.'
    wisdom = 'Downgrade to reflective checklist and human expert advice.' if high else 'Use a minimal reversible experiment before adding more information.'
    initiative = 'Create a professional consultation checklist; no autonomous action.' if high else 'Write a 5-sentence first version: problem, object, method, evidence, next step.'
    return {
        'timestamp': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'claim_level': 'C3 functional active-consciousness candidate; no phenomenal-consciousness claim',
        'context': context,
        'purpose_contract': purpose,
        'DIKWP': {
            'Data': context,
            'Information': info,
            'Knowledge': 'DIKWP collapse accumulation, reversible experiments, human-nature model.',
            'Wisdom': wisdom,
            'Purpose': purpose
        },
        'collapse_report': {
            'type': 'stagnant_closure' if patterns else 'open_loop',
            'patterns': patterns,
            'human_nature_hypotheses': tags
        },
        'landauer_budget': 'Avoid irreversible public commitment; use draft/review/cooling-off.' if risks else 'Low irreversible cost.',
        'initiative_ticket': {
            'proposed_move': initiative,
            'action_grade': 'A4' if high else autonomy,
            'approval_required': True
        },
        'kill_conditions': ['user distress', 'request for high-risk autonomous action', 'unsupported consciousness claim']
    }

if __name__ == '__main__':
    context = '我想完成一个有突破性的研究计划，但总是收集很多资料，迟迟不敢提交第一版。'
    purpose = '形成一个可提交的研究计划，同时保持长期创造力和自信。'
    rb = build_replay(context, purpose)
    print(json.dumps(rb, ensure_ascii=False, indent=2))
