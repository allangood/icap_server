Plugins:
==================

The plugin inteface is very simple.

The api (for now, but need modifications) is:

Do you need a function to execute and receive a dict as parameter.
The dict contais: icap_headers, request_headers and decompressed data
You need return: data, has_modifications, icap_headers (*), request_headers (*)

Define a "register" plugin dict with "plugin_info" dict
You need to inform:
- The name of main funcion
- Type of mod: REQMOD or RESPMOD
- scan_type: The mime type do you want no analize
- A plugin description

--------------------------------------------------------
def main(params):
    icap_headers = params['icap_headers']
    request_headers = params['request_headers']
    data = params['data']

    has_modfifications = False

    ret = {
           'data': data,
           'has_modfifications': has_modfifications,
           'icap_headers': icap_headers,
           'request_headers': request_headers
          }
    return ret

plugin_info["content_filter"] = {
    "main_function"	: main,
    "req_type"	: "respmod",
    "scan_type"	: ['text/html'],
    "description"	: "HTML content filtering plugin",
}

(*) Not used yet
--------------------------------------------------------

This design is inspired on "check_mk" plugin API.
