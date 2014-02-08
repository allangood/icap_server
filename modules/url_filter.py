def main(params):
  icap_headers = params.icap_headers
  request_headers = params.request_headers
  data = params.data
  ret = {'data': data, 'icap_headers': icap_headers, 'request_headers': request_headers}
  return ret

plugin_info["url_filter"] = {
	"main_function"	: main,
	"req_type"	: "reqmod",
	"scan_content"	: False,
	"description"	: "URL filtering plugin",
}
