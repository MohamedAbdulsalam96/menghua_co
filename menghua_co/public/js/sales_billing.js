frappe.ui.form.on("Sales Billing", {
    refresh: function(frm) {
        if (frm.doc.docstatus === 1 && frm.doc.outstanding_amount !== 0) {
            frm.add_custom_button(__("Payment"), function() {
                frm.call({
                    method: "menghua_co.custom.sales_billing.make_payment_entry",
                    args: {
                        source_name: frm.doc.name
                    },
                    callback: function(response) {
                        if (response && !response.exc) {
                            frappe.model.open_mapped_doc({
                                method: "menghua_co.custom.sales_billing.make_payment_entry",
                                frm: cur_frm,
                            });
                        }
                    }
                });
            }, __("Action"));

            frm.page.set_inner_btn_group_as_primary(__("Action"));
        }
    }
});
