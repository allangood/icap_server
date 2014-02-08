Plugins:
==================

The plugin inteface is very simple.

The api (for now, but need modifications) is:

# Do you need a function to execute and receive a dict as parameter.
def main(params):
    # The dict contais: icap_headers, request_headers and decompressed data
    icap_headers = params['icap_headers']
    request_headers = params['request_headers']
    data = params['data']

    has_modfifications = False

    # You need return: data, has_modifications, icap_headers (*), request_headers (*)
    ret = {
           'data': data,
           'has_modfifications': has_modfifications,
           'icap_headers': icap_headers,
           'request_headers': request_headers
          }
    return ret

# And this is the "register" plugin dict
# You need to inform:
# - The name of main funcion
# - Type of mod: REQMOD or RESPMOD
# - scan_type: The mime type do you want no analize
# - A plugin description

plugin_info["content_filter"] = {
    "main_function"	: main,
    "req_type"	: "respmod",
    "scan_type"	: ['text/html'],
    "description"	: "HTML content filtering plugin",
}

(*) Not used yet

This design is inspired on "check_mk" plugin API.
