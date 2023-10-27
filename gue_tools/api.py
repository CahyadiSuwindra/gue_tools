import frappe

def todo_has_permission(doc, ptype="read", user=None):
  user = user or frappe.session.user
	todo_roles = frappe.permissions.get_doctype_roles("ToDo", ptype)
	todo_roles = set(todo_roles) - set(AUTOMATIC_ROLES)

	if any(check in todo_roles for check in frappe.get_roles(user)):
		return True
	else:
		return doc.allocated_to == user or doc.assigned_by == user
