import React from "react";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";
import { addReview } from "../api/reviews";

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
      onSubmit={async (values, { setSubmitting, resetForm }) => {
        try {
          const payload = {
            deviceId: deviceId,
            user_id: values.user_id, // Store the raw user ID
            rating: values.rating,
            comment: values.comment,
            created_at: new Date().toISOString(),
          };

          const data = await addReview(payload);
          onAdded(data);
          resetForm();
        } catch (e) {
          console.error(e);
          alert("Failed: " + e.message);
        }
        setSubmitting(false);
      }}
    >
      {({ isSubmitting }) => (
        <Form className="form-card">
          <label>Your user id (demo)</label>
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
