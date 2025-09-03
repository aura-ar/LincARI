# Use the same base image as the current devcontainer
FROM lcas.lincoln.ac.uk/lcas/pal-gallium-pal-metapkg-development-ari:35-dev

# Set working directory
WORKDIR /workspace

# Add ROS apt key
RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -

# Source the PAL Gallium setup and update packages
RUN bash -c "source /opt/pal/gallium/setup.bash && \
    apt update && \
    apt upgrade -y && \
    rosdep init && \
    rosdep update"

# Install additional packages
RUN apt install -y \
    iproute2 \
    iputils-ping \
    pulseaudio-utils \
    alsa-utils \
    python3-pyaudio
    
# Add root user to the audio group
RUN usermod -aG audio root

# Set appropriate permissions for the PulseAudio socket and cookie
RUN echo '#!/bin/bash\n\
echo "Setting permissions for PulseAudio socket..."\n\
chmod 777 "/run/user/$(id -u)/pulse" 2>/dev/null || true\n\
\n\
if [ -f "/root/.config/pulse/cookie" ]; then\n\
    echo "Fixing ownership of PulseAudio cookie..."\n\
    chown root:root /root/.config/pulse/cookie\n\
    chmod 600 /root/.config/pulse/cookie\n\
else\n\
    echo "PulseAudio cookie not found at /root/.config/pulse/cookie. Skipping ownership fix."\n\
fi' > /usr/local/bin/setup-pulse.sh && \
    chmod +x /usr/local/bin/setup-pulse.sh

# Run the PulseAudio setup script at container start
RUN echo '/usr/local/bin/setup-pulse.sh' >> /root/.bashrc

# Add the source command to bashrc so it's available in interactive shells
RUN echo "source /opt/pal/gallium/setup.bash" >> /root/.bashrc

# Set environment variables
ENV ROS_LOCALHOST_ONLY=0
ENV LIBGL_ALWAYS_SOFTWARE=1

# Copy workspace contents
COPY . /workspace/

# Set the default command
CMD ["/bin/bash"]