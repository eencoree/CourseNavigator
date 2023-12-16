SELECT step.*
FROM step
JOIN content ON step.id_step = content.step_id
JOIN course ON content.id_course = course.id_course
WHERE LOWER(course.title) = LOWER('название курса');
