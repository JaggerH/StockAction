import os
import re

def replace_by_dict(text, replacements):
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text

def match_security(text):
    trandition_to_simple = {'壹': '一', '贰': '二', '叁': '三', '肆': '四', '伍': '五', '陆': '六', '柒': '七', '捌': '八', '玖': '九','〇':'零'}
    common_used_ch_numerals = {'幺': '1','零': '0', '一': '1', '二': '2', '两': '2', '三': '3', '四': '4', '五': '5', '六': '6', '七': '7', '八': '8', '九': '9'}

    update_text = replace_by_dict(text, trandition_to_simple)
    update_text = replace_by_dict(update_text, common_used_ch_numerals)

    match = re.search(r'\d{6}', update_text)
    if match:
        return update_text, match.group()
    else:
        return update_text, None

def extract_segment(text, word, pre, after):
    segments = text.split("，")
    indexs = [idx for idx, segment in enumerate(segments) if word in segment]
    
    texts = []
    for idx in indexs:
        start_idx = max(0, idx - pre)
        end_idx = min(idx + after, len(segments))

        text = "，".join(segments[start_idx:end_idx])
        texts.append(text)

    return texts

def match_security_in_text(text, debug=True):
    segements = extract_segment(text, "福利", 0, 5)
    securities = []
    for segement in segements:
        updated_text, security = match_security(segement)
        if security:
            if debug:
                print(security)
                print(updated_text)
            securities.append(security)

    return securities