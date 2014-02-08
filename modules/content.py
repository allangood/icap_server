def main(params):
    icap_headers = params['icap_headers']
    request_headers = params['request_headers']
    data = params['data']
    if (len(data) > 0):
        mod3 = data.replace('Pizzolato', '-*-')
        has_modfifications = True
    else:
        mod3 = data
        has_modfifications = False
    ret = {'data': mod3, 'has_modfifications': has_modfifications, 'icap_headers': icap_headers, 'request_headers': request_headers}
    return ret

plugin_info["content_filter"] = {
    "main_function"		: main,
    "req_type"		: "respmod",
    "scan_type"		: ['text/html'],
    "description"		: "HTML content filtering plugin",
}
