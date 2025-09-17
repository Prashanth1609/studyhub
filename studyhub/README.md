# StudyHub - Study Session Management Platform

A Django-based web application for organizing and joining study sessions. Users can create virtual or in-person study sessions, join existing ones, and communicate through built-in messaging.

## Features

- **Session Management**: Create, view, join, and leave study sessions
- **Virtual & In-Person Support**: Sessions can be virtual (with meeting links) or in-person (with locations)
- **Subject Tagging**: Categorize sessions by subjects (Math, Physics, CS, etc.)
- **Capacity Management**: Limit session participants
- **Real-time Messaging**: Chat functionality within sessions
- **Search & Filtering**: Filter sessions by subject, type, and search terms
- **Responsive Design**: Works on desktop and mobile devices
- **REST API**: Full API support for integration

## Recent Fixes Applied

### 1. URL Pattern Issues
- **Fixed**: URL patterns in `core/urls.py` were missing proper parameters
- **Solution**: Added proper URL patterns with `pk` parameters for session details
- **Added**: Join/leave session endpoints

### 2. Template Structure Issues
- **Fixed**: Templates were minimal and lacked proper HTML structure
- **Solution**: Completely redesigned all templates with:
  - Proper HTML5 structure
  - Responsive design
  - Better user experience
  - Form validation display
  - Interactive elements

### 3. Form Functionality Issues
- **Fixed**: Forms lacked proper styling and validation feedback
- **Solution**: Enhanced forms with:
  - Field-specific error display
  - Better styling and layout
  - JavaScript for dynamic field toggling
  - Proper form validation

### 4. Navigation Issues
- **Fixed**: Navigation was broken and inconsistent
- **Solution**: Created proper navigation with:
  - User authentication status
  - Proper URL routing
  - Consistent styling

### 5. Message Functionality
- **Added**: Message posting functionality in session details
- **Enhanced**: Message display with proper formatting

## Installation & Setup

1. **Clone the repository** (if not already done)
2. **Activate virtual environment**:
   ```bash
   source env/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. **Load sample data**:
   ```bash
   python manage.py create_sample_data
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Sample Users

The management command creates these sample users:
- **john_doe** (password: password123)
- **jane_smith** (password: password123)
- **mike_wilson** (password: password123)
- **admin** (superuser)

## Usage

### For Students
1. **Browse Sessions**: Visit the home page to see upcoming study sessions
2. **Filter & Search**: Use the search and filter options to find relevant sessions
3. **Join Sessions**: Click on session details and join if there's space
4. **Participate**: Send messages and interact with other members

### For Session Hosts
1. **Create Sessions**: Click "Create Session" to start a new study group
2. **Set Details**: Choose virtual or in-person, set capacity, add subjects
3. **Manage**: Monitor participants and respond to messages

## API Endpoints

The application also provides a REST API:

- `GET /api/sessions/` - List all sessions
- `POST /api/sessions/` - Create a new session
- `GET /api/sessions/{id}/` - Get session details
- `POST /api/sessions/{id}/join/` - Join a session
- `POST /api/sessions/{id}/leave/` - Leave a session
- `GET /api/tags/` - List all subject tags

## Technical Details

### Models
- **StudySession**: Main session model with all session details
- **SubjectTag**: Subject categories for sessions
- **SessionMember**: Junction table for session participants
- **Message**: Chat messages within sessions

### Views
- **Function-based views**: For web interface
- **DRF ViewSets**: For API functionality
- **Proper authentication**: Login required for certain actions

### Templates
- **Responsive design**: Works on all screen sizes
- **Modern UI**: Clean, professional appearance
- **Interactive elements**: Dynamic forms and real-time updates

## File Structure

```
studyhub/
├── core/                    # Main application
│   ├── models.py           # Database models
│   ├── views.py            # View logic
│   ├── urls.py             # URL routing
│   ├── forms.py            # Form definitions
│   ├── serializers.py      # API serializers
│   ├── templates/          # HTML templates
│   └── management/         # Management commands
├── studyhub/               # Project settings
│   ├── settings.py         # Django settings
│   └── urls.py             # Main URL configuration
├── static/                 # Static files (CSS, JS)
└── manage.py               # Django management script
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.
