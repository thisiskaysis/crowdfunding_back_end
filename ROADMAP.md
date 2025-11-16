=== Crowdfunding Website Backend Roadmap ===

---

## 1. Initial Breakdown and Considerations

### Project Type:
- Website (Crowdfunding platform aimed at children/parents for school, sports, extracurricular costs)

### Backend Tech Stack:
- Django (Python framework)
- Database: SQLite (for study project, later switch to full database)

### Key Features Suggestions:

#### User Management
- Parent accounts (main users)
- Child profiles linked to parent accounts
- Authentication (signup/login/logout, password reset)
- Profile management (update personal info, child info)

#### Campaign Management
- Create campaigns for child-related needs
- Campaign details: title, description, target amount, deadline, images
- Track donations received
- Edit/cancel campaigns (by parent)

#### Donation System
- Users can donate to a campaign
- Track donor info (optional: anonymous donations)
- Payment integration (mock for now)

#### Dashboard / Analytics
- Parent dashboard: total raised, campaign status, donation history
- Optional admin dashboard: site-wide stats, manage users and campaigns

#### Notifications / Communication
- Email notifications for donations, updates, reminders
- Optional: comment system on campaigns

#### Security & Permissions
- Only parents can create campaigns
- Only linked parent can manage their child’s campaigns
- Ensure donations are safe and private

---

## 2. High-Level Backend Flowchart (Conceptual)

```
[Client (Browser)]
        |
        v
[HTTP Request to Django Server]
        |
        v
[URL Routing] --> [Views / API Endpoints]
        |
        v
[Business Logic]
        |           \
        v            \
[Database Operations]  [External Services (Payment, Email)]
        |
        v
[Response Back to Client]
```

### Example Endpoint Flow: Creating a Campaign
```
[User submits campaign form]
        |
        v
[POST request to /campaign/create/]
        |
        v
[View checks authentication & permissions]
        |
        v
[View validates form data]
        |
        v
[Save campaign to Database]
        |
        v
[Return success message / redirect to campaign page]
```

### Example: Making a Donation
```
[User clicks "Donate" button]
        |
        v
[POST request to /donation/<campaign_id>/]
        |
        v
[Validate donation amount]
        |
        v
[Process payment (mock)]
        |
        v
[Save donation to Database]
        |
        v
[Update Campaign.amount_raised]
        |
        v
[Return success message]
```

---

## 3. Development Roadmap / Checklist

### Phase 1 – Core Backend
1. Set up Django project and SQLite database  
2. Create `User` model (use Django’s built-in auth)  
3. Create `Child` model linked to parent  
4. Set up CRUD endpoints for Users, Children, Campaigns

### Phase 2 – Donation System
1. Create `Donation` model (linked to Campaign and User)  
2. Implement mock payment flow  
3. Track total donations per campaign

### Phase 3 – Dashboard & Analytics
1. Parent dashboard: list of campaigns, total raised, donation history  
2. Optional admin dashboard: user & campaign management

### Phase 4 – Notifications & Extras
1. Email notifications (Django’s `send_mail`)  
2. Optional comments/updates system for campaigns

### Phase 5 – Security & Validation
1. Permissions: only parents can create/edit campaigns for their child  
2. Input validation & error handling  
3. Optional: admin moderation of campaigns

---

## 4. Detailed Flowchart: Models & Relationships

### Models & Relationships
```
User (Parent)
├─ id
├─ username / email / password
├─ profile info (name, contact, etc.)
└─ has_many → Children

Child
├─ id
├─ parent_id (FK to User)
├─ name
├─ age
└─ has_many → Campaigns

Campaign
├─ id
├─ child_id (FK to Child)
├─ title
├─ description
├─ goal_amount
├─ amount_raised
├─ deadline
├─ image_url
└─ has_many → Donations

Donation
├─ id
├─ campaign_id (FK to Campaign)
├─ donor_name / donor_email
├─ amount
├─ timestamp
└─ payment_status
```

### Endpoints / Views (Django)

**User / Parent**
```
POST /signup/  
POST /login/  
GET /profile/  
PUT /profile/
```

**Child**
```
POST /child/create/  
GET /child/<id>/  
PUT /child/<id>/  
DELETE /child/<id>/
```

**Campaign**
```
POST /campaign/create/  
GET /campaign/<id>/  
PUT /campaign/<id>/  
DELETE /campaign/<id>/  
GET /campaigns/
```

**Donation**
```
POST /donation/<campaign_id>/  
GET /donation/<campaign_id>/
```

### Example: Request Flow (Donation)
```
[Client Browser]
        |
        v
POST /donation/<campaign_id>/ (with donation data)
        |
        v
[Django URL Routing → View Function]
        |
        v
[Check Authentication & Permissions]
        |
        v
[Validate Donation Amount]
        |
        v
[Process Payment (mock or real)]
        |
        v
[Save Donation in Database]
        |
        v
[Update Campaign.amount_raised]
        |
        v
[Send Response → Client Browser]
```

### Optional Extras in Flow
- Send Email Confirmation after donation  
- Update Parent Dashboard  
- Admin Panel → view/manage all Users, Children, Campaigns, Donations

---

## 5. Visual ER + Flow Diagram (Text Version)

```
+-----------------+       1       +-----------------+
|     User        |---------------|      Child      |
|-----------------|   has_many    |-----------------|
| id              |               | id              |
| username/email  |               | parent_id (FK)  |
| password        |               | name            |
| name            |               | age             |
+-----------------+               +-----------------+
       |                                 |
       | owns_many                        | has_many
       v                                 v
+-----------------+       1       +-----------------+
|    Campaign     |---------------|    Donation     |
|-----------------|   has_many    |-----------------|
| id              |               | id              |
| child_id (FK)   |               | campaign_id(FK) |
| title           |               | donor_name      |
| description     |               | donor_email     |
| goal_amount     |               | amount          |
| amount_raised   |               | timestamp       |
| deadline        |               | payment_status  |
| image_url       |               +-----------------+
+-----------------+
```

---

This document contains **everything from initial breakdown, suggested features, flowcharts, endpoints, models, relationships, and request flows**. It is structured to guide development in Django from start to finish.

