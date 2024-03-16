# list of transformations from https://arxiv.org/pdf/2002.05709v3.pdf (Figure 5)

TRANSFORMATIONS_DATA = \
    [(56.3, 'Crop', 'Color'),
     (55.8, 'Color', 'Crop'),
     (46.2, 'Sobel', 'Crop'),
     (40.6, 'Sobel', 'Cutout'),
     (40.0, 'Cutout', 'Sobel'),
     (39.9, 'Crop', 'Noise'),
     (39.2, 'Crop', 'Average'),
     (38.8, 'Noise', 'Crop'),
     (35.5, 'Color', 'Cutout'),
     (35.1, 'Blur', 'Crop'),
     (33.9, 'Cutout', 'Color'),
     (33.1, 'Cutout', 'Crop'),
     (33.1, 'Crop', None),  # Single transformation
     (30.2, 'Crop', 'Rotate'),
     (30.0, 'Rotate', 'Crop'),
     (29.4, 'Cutout', 'Average'),
     (26.5, 'Cutout', 'Noise'),
     (25.8, 'Noise', 'Cutout'),
     (25.7, 'Color', 'Average'),
     (25.6, 'Cutout', None),  # Single transformation
     (25.2, 'Blur', 'Cutout'),
     (25.2, 'Cutout', 'Blur'),
     (22.5, 'Rotate', 'Cutout'),
     (22.5, 'Crop', 'Cutout'),
     (22.4, 'Cutout', 'Rotate'),
     (21.0, 'Color', 'Noise'),
     (20.9, 'Sobel', 'Color'),
     (20.7, 'Rotate', 'Color'),
     (18.8, 'Color', 'Sobel'),
     (18.8, 'Sobel', 'Average'),
     (18.8, 'Color', None),  # Single transformation
     (16.6, 'Blur', 'Color'),
     (16.5, 'Color', 'Rotate'),
     (15.5, 'Noise', 'Average'),
     (14.5, 'Blur', 'Average'),
     (13.8, 'Rotate', 'Average'),
     (11.4, 'Color', 'Blur'),
     (9.8, 'Noise', 'Blur'),
     (9.7, 'Rotate', 'Noise'),
     (9.7, 'Blur', 'Noise'),
     (9.6, 'Noise', 'Rotate'),
     (9.3, 'Sobel', 'Blur'),
     (7.6, 'Noise', 'Sobel'),
     (7.6, 'Noise', None),  # Single transformation
     (7.5, 'Noise', 'Color'),
     (6.5, 'Rotate', 'Blur'),
     (6.2, 'Sobel', 'Rotate'),
     (5.8, 'Blur', 'Sobel'),
     (4.3, 'Rotate', None),  # Single transformation
     (4.3, 'Rotate', 'Sobel'),
     (4.0, 'Sobel', 'Noise'),
     (4.0, 'Sobel', None),  # Single transformation
     (2.6, 'Blur', 'Rotate'),
     (2.6, 'Blur', None)]  # Single transformation