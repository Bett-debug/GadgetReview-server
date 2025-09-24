import React from "react";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";

const API_URL = "http://localhost:3001";

function addReview(review) {
  return fetch(`${API_URL}/reviews`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(review),
  }).then((res) => {
    if (!res.ok) throw new Error("Failed to add review");
    return res.json();
  });
}

const ReviewSchema = Yup.object().shape({
  user_id: Yup.number().required("User id required").integer().positive(),
  rating: Yup.number().required("Rating required").min(1).max(5),
  comment: Yup.string().required("Please add a comment").min(5),
});

export default function ReviewForm({ deviceId, onAdded }) {
  return (
    <Formik
      initialValues={{ user_id: 1, rating: 5, comment: "" }}
      validationSchema={ReviewSchema}
      onSubmit={(values, { setSubmitting, resetForm }) => {
        const payload = {
          deviceId: deviceId,
          user_id: values.user_id,
          rating: values.rating,
          comment: values.comment,
          created_at: new Date().toISOString(),
        };

        addReview(payload)
          .then((data) => {
            onAdded(data);
            resetForm();
          })
          .catch((e) => {
            console.error(e);
            alert("Failed: " + e.message);
          })
          .finally(() => setSubmitting(false));
      }}
    >
      {({ isSubmitting }) => (
        <Form className="form-card">
          <label>Your user id</label>
          <Field name="user_id" type="number" />
          <ErrorMessage
            name="user_id"
            component="div"
            className="field-error"
          />

          <label>Rating</label>
          <Field as="select" name="rating">
            <option value={5}>5 - Excellent</option>
            <option value={4}>4 - Very good</option>
            <option value={3}>3 - Good</option>
            <option value={2}>2 - Poor</option>
            <option value={1}>1 - Terrible</option>
          </Field>
          <ErrorMessage name="rating" component="div" className="field-error" />

          <label>Comment</label>
          <Field as="textarea" name="comment" rows="3" />
          <ErrorMessage
            name="comment"
            component="div"
            className="field-error"
          />

          <div className="form-actions">
            <button
              type="submit"
              disabled={isSubmitting}
              className="btn primary"
            >
              Post Review
            </button>
          </div>
        </Form>
      )}
    </Formik>
  );
}
