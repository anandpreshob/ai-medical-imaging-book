# Chapter 6 image prompts

Generated with the built-in image generation tool on 2026-08-30.

## `classification-example.png`

Scientific-educational landscape infographic showing a single chest radiograph treated as one whole input and mapped to image-level probabilities for pneumonia, pleural effusion, and pneumothorax. Emphasize WHAT is present and “No location output.” Do not show boxes, heatmaps, masks, or pathology pointers. Use a warm off-white canvas, grayscale radiograph, restrained teal/navy/cyan/coral palette, crisp vector-like forms, and large legible typography.

## `object-detection-example.png`

Scientific-educational landscape infographic showing an axial lung CT with exactly three pulmonary nodules localized by separate bounding boxes and confidence scores. Include one subtle possible missed candidate and a result card summarizing boxes, classes, and scores. Emphasize WHAT + WHERE and approximate location. Do not show segmentation masks. Use a warm off-white canvas, grayscale CT, restrained teal/navy/cyan/coral palette, crisp vector-like forms, and large legible typography.

## `semantic-segmentation-example.png`

Scientific-educational landscape infographic showing a grayscale axial brain MRI beside the same image with smooth class masks for gray matter, white matter, ventricles, tumor, and background. Emphasize WHAT IS EACH PIXEL and one class per pixel. Do not show boxes or object identities. Use a warm off-white canvas, grayscale MRI, colorblind-aware teal/cyan/navy/violet/coral masks, crisp vector-like forms, and large legible typography.

## `instance-segmentation-example.png`

Scientific-educational landscape infographic showing an H&E histology field beside an overlay in which each nucleus has a distinct colored mask and crisp boundary, including visibly separated touching nuclei. Add a count card and emphasize WHICH OBJECT, separate/count/measure, and one identity per object. Do not show boxes or one shared semantic color. Use a warm off-white canvas, natural pink-purple H&E, varied accessible instance colors, crisp vector-like forms, and large legible typography.
