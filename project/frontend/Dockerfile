FROM nginx:alpine

# Copy pre-built static files into Nginx's default directory
COPY . /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
