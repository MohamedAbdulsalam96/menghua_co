frappe.ui.form.on("Quotation", {
    refresh(frm) {
        frm.set_query("item_code", "items", function (doc, cdt, cdn) {
            return {
                filters: {
                    'is_sales_item': 1,
                    'custom_allow_standard_type': frm.doc.custom_allow_standard_type === 1 || frm.doc.custom_mh_order_type === "หน้าร้าน" ? 1 : undefined,
                    'custom_allow_custom_type': frm.doc.custom_allow_custom_type === 1 || frm.doc.custom_mh_order_type === "สั่งทำ" ? 1 : undefined
                }
            };
        });
    },
    custom_mh_order_type: function(frm) {
        frm.refresh_field("items");
    }
});
