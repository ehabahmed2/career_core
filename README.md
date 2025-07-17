# Career Core – Recruitment Platform

Career Core Recruitment Solutions is a full-featured recruitment management system that bridges the gap between companies with open positions, experienced recruiters, and qualified job seekers.

---

## 🚀 Project Overview

Career Core provides a robust ecosystem with specialized portals and tools for:

- 🔹 **Companies**: Easily post and manage job openings
- 🔹 **Recruiters**: Manage candidates and recruitment pipelines
- 🔹 **Candidates**: Discover and apply to relevant positions

---

## ✅ Completed Features

### 👤 **User System Implementation**
- Three-tier role-based access (Admin / Head Recruiter / Recruiter)
- Editable user profiles
- Admin-controlled recruiter approval workflow

### 📊 **Dashboard Functionality**

#### **Admin Dashboard**
- Recruiter lifecycle management (approve / suspend / delete)
- Full CRUD for job offers
- Candidate tracking with status updates
- Export data to Excel
- Manage testimonials and team member listings

#### **Recruiter Dashboard**
- **Head Recruiter**:
  - Create and manage job offers
- **Recruiter**:
  - View assigned job offers
- Candidate tracking per recruiter
- Export candidate data to Excel

### 🌐 **Public-Facing Components**
- Responsive job board with advanced filtering
- Streamlined application process
- SEO-optimized pages with structured schema markup
- GDPR-compliant cookie consent

### 🧭 **Navigation & UI**
- Dynamic, role-based navigation
- Intuitive profile editing
- Offer and candidate status visibility
- Fully mobile-responsive design

---

## 🛠️ Technical Highlights

### 🔐 **Security**
- Role-based access control (RBAC)
- CSRF protection across forms
- Strict data ownership and validation

### ⚡ **Performance**
- Optimized and annotated ORM queries
- Lazy-loading for high-traffic images
- Database query optimization for large datasets

### 💡 **UX Features**
- Color-coded statuses (Green = Hired, Orange = In Progress, Red = Rejected)
- Toast notifications for user feedback
- Confirmation modals for critical actions
- Data export tools (Excel-friendly format)

---

## 🧰 Maintenance Notes

### 1. Offer Visibility
- Suspended offers are automatically hidden from the public
- Offer visibility toggled via dashboard controls

### 2. Recruiter Permissions

```python
# Example permission check in views
if user.is_head_recruiter or user.is_admin:
```
## 🔄 Candidate Tracking Workflow

A streamlined recruitment pipeline ensures all candidates are tracked and managed efficiently.

### **Status Pipeline**
`New → Review → Interview → Hired / Rejected`

- Candidates automatically move through stages as actions are taken
- Visual indicators and filters available in dashboards
- Recruiters only see and manage their assigned candidates
- Admin has global access to all candidate data

---

## 🖼️ Screenshot Placeholders

_Recommended screenshots to include:_

- 🖥️ **Desktop & Mobile Home Page**  
  > Showcase the public-facing job board and responsive layout

- 📊 **Admin Dashboard Interface**  
  > Highlight tools for recruiter/job/candidate management

- 👥 **Recruiter Candidate View**  
  > Display assigned candidates and status pipelines

- 📄 **Job Listing Page**  
  > Show filtering, application forms, and structured layout

- 🌟 **Testimonial & Team Management**  
  > Demonstrate editable team and testimonial sections via the admin panel

> _Place these images in a `/screenshots/` directory or embed them using markdown:_
> ```markdown
> ![Dashboard Preview](screenshots/admin-dashboard.png)
> ```

---

## 🔑 Client Access Details

### 🔧 Admin Portal
- **URL**: `/admin-dashboard/`
- **Features**:
  - Full access to recruiter management, job offers, candidate tracking
  - Control over public-facing testimonials and team sections
  - Excel export for offers and candidate databases

### 🧑‍💼 Recruiter Portal
- **URL**: `/recruiter-dashboard/`
- **Features**:
  - **Head Recruiters**: Can manage job offers and candidates
  - **Recruiters**: Can view job offers and manage their assigned candidates
  - Candidate export and status management

---

## 📌 Project Status

🟢 **Production Ready & Maintained**

- Fully functional and live with core features
- Built to scale with additional modules like:
  - Email notifications
  - Analytics dashboards
  - Interview scheduling tools

---

## 📄 License

© 2025 **Career Core Recruitment Solutions**  
All rights reserved. Redistribution or modification of this platform without permission is prohibited.

---