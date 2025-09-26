import React from "react";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";

const API_URL = "http://localhost:5000/api";

const AddDeviceSchema = Yup.object().shape({
  name: Yup.string().required("Required"),
  brand: Yup.string().required("Required"),
  category: Yup.string().required("Required"),
  avg_price: Yup.number()
    .typeError("Must be a number")
    .positive("Must be positive")
    .required("Required"),

  image_url: Yup.string().url("Must be a valid URL").nullable(),
  recommended_store: Yup.string().url("Must be a valid URL").nullable(),
  specs: Yup.string().nullable(),
});

export default function AddDeviceForm({ onSuccess }) {
  return (
    <Formik
      initialValues={{
        name: "",
        brand: "",
        category: "",
        avg_price: "",
        image_url: "",
        recommended_store: "",
        specs: "",
      }}
      validationSchema={AddDeviceSchema}
      onSubmit={async (values, { setSubmitting, resetForm }) => {
        try {
          const res = await fetch(`${API_URL}/devices`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ ...values, status: "pending" }),
          });
          if (!res.ok) {
            const err = await res.json();
            alert("Failed: " + (err.message || JSON.stringify(err)));
          } else {
            const data = await res.json();
            resetForm();
            if (onSuccess) onSuccess(data);
            alert("Device suggested successfully (pending approval).");
          }
        } catch (e) {
          console.error(e);
          alert("Network error");
        }
        setSubmitting(false);
      }}
    >
      {({ isSubmitting }) => (
        <Form className="form-card">
          <label>Name</label>
          <Field name="name" placeholder="e.g. iPhone 14 Pro" />
          <ErrorMessage name="name" component="div" className="field-error" />

          <label>Brand</label>
          <Field name="brand" placeholder="Apple, Samsung..." />
          <ErrorMessage name="brand" component="div" className="field-error" />

          <label>Category</label>
          <Field as="select" name="category">
            <option value="">Select</option>
            <option value="phone">Phone</option>
            <option value="laptop">Laptop</option>
            <option value="tablet">Tablet</option>
          </Field>
          <ErrorMessage
            name="category"
            component="div"
            className="field-error"
          />

          <label>Average price</label>
          <Field name="avg_price" placeholder="e.g. Ksh 89900" />
          <ErrorMessage
            name="avg_price"
            component="div"
            className="field-error"
          />

          <label>Image URL</label>
          <Field name="image_url" placeholder="https://..." />
          <ErrorMessage
            name="image_url"
            component="div"
            className="field-error"
          />

          <label>Recommended store (URL)</label>
          <Field name="recommended_store" placeholder="https://..." />
          <ErrorMessage
            name="recommended_store"
            component="div"
            className="field-error"
          />

          <label>Key specs (short)</label>
          <Field
            as="textarea"
            name="specs"
            rows="4"
            placeholder="e.g. 8GB RAM, 128GB storage..."
          />

          <div className="form-actions">
            <button
              type="submit"
              disabled={isSubmitting}
              className="btn primary"
            >
              Suggest Device
            </button>
          </div>
        </Form>
      )}
    </Formik>
  );
}
