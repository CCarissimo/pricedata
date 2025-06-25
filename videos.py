import streamlit as st
import streamlit.components.v1 as components

html_string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Video Gallery</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Font: Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f0f2f5; /* Light grey background */
        }
        /* Custom styles for video responsiveness (aspect ratio) */
        .video-container {
            position: relative;
            padding-bottom: 56.25%; /* 16:9 aspect ratio */
            height: 0;
            overflow: hidden;
            border-radius: 0.75rem; /* rounded corners */
        }
        .video-container iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
    </style>
</head>
<body class="p-6 md:p-10 lg:p-12">
    <div class="max-w-7xl mx-auto bg-white p-6 md:p-8 lg:p-10 rounded-xl shadow-lg">
        <h1 class="text-3xl md:text-4xl font-bold text-gray-800 mb-8 text-center">Featured Videos</h1>
        
        <!-- Video 1 -->
        <div class="mb-10 p-4 border border-gray-200 rounded-xl shadow-md">
            <h2 class="text-2xl font-semibold text-gray-700 mb-3">The Algorithm Game</h2>
            <p class="text-gray-600 mb-5">
                This video is a presentation on the Algorithm Game, introducing the meta-game of Algorithm design.
            </p>
            <div class="video-container">
                <!-- YouTube embed code for the first video -->
                <iframe
                    src="https://www.youtube.com/embed/McXM1380Ii4"
                    title="YouTube video player 1"
                    frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen
                    class="rounded-lg"
                ></iframe>
            </div>
            <p class="text-sm text-gray-500 mt-4">
                Source: YouTube.
            </p>
        </div>

        <!-- Video 2 -->
        <div class="p-4 border border-gray-200 rounded-xl shadow-md">
            <h2 class="text-2xl font-semibold text-gray-700 mb-3">The Algorithm Game - Extended Lecture</h2>
            <p class="text-gray-600 mb-5">
                This video is a lecture on the Algorithm Game, which goes into greater depth on the the meta-game of 
                Algorithm design.
            </p>
            <div class="video-container">
                <!-- YouTube embed code for the second video -->
                <iframe
                    src="https://www.youtube.com/embed/FHlARQQoD-w"
                    title="YouTube video player 2"
                    frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen
                    class="rounded-lg"
                ></iframe>
            </div>
            <p class="text-sm text-gray-500 mt-4">
                Source: YouTube.
            </p>
        </div>
    </div>
</body>
</html>
"""

components.html(html_string, height=2000)

# VIDEO_URL = "https://www.youtube.com/watch?v=McXM1380Ii4&t=3s"
# st.video(VIDEO_URL)
#
# second_url = "https://www.youtube.com/watch?v=FHlARQQoD-w"
# st.video(second_url)

