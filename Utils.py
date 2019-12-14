from Constants import *

def replaceHtml(email, sample_html):
    email_payload = SAMPLE_PAYLOAD[email]
    key_list = list(email_payload.keys())
    value_list = list(email_payload.values())
    updated_html = sample_html
    for counter in range(len(key_list)):
        updated_html = updated_html.replace("{"+key_list[counter]+"}", value_list[counter])
    return updated_html
