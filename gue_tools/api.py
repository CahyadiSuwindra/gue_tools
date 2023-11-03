import frappe
from google.cloud import storage

def todo_has_permission(doc, ptype="read", user=None):
	user = user or frappe.session.user
	todo_roles = frappe.permissions.get_doctype_roles("ToDo", ptype)
	todo_roles = set(todo_roles) - set(AUTOMATIC_ROLES)

	if any(check in todo_roles for check in frappe.get_roles(user)):
		return True
	else:
		return doc.allocated_to == user or doc.assigned_by == user
		
def upload_cs_file(bucket_name, source_file_name, destination_file_name): 
	fpath = frappe.get_site_path()

	os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = fpath+"/mp-gcp-rnd-91c05a8a4585.json"
	gcp_client = storage.Client()

	bucket = gcp_client.bucket('inttools-storage')

	blob = bucket.blob('site_config.json')
	blob.upload_from_filename(fpath+'/site_config.json')
	
	return True

