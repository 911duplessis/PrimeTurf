# PrimeTurf Lead CRM — Setup Guide

This connects the website contact form to a Google Sheet (a simple CRM) and
sends an email notification to **leonve33@gmail.com** for every enquiry.
No paid services required — everything runs on Google's free tier.

## 1. Create the Google Sheet

1. Go to [sheets.google.com](https://sheets.google.com) and create a new
   spreadsheet named **PrimeTurf Leads**.
2. Rename the default tab ("Sheet1") to **Leads** — double-click the tab
   name at the bottom.
3. In row 1, add these column headers exactly, one per cell (A1 through J1):

   | A | B | C | D | E | F | G | H | I | J |
   |---|---|---|---|---|---|---|---|---|---|
   | Timestamp | Name | Phone | Email | Estate/Area | Project Type | Message | Status | Notes | Follow-up Date |

## 2. Add the Apps Script

1. In the spreadsheet, go to **Extensions → Apps Script**.
2. Delete any starter code shown in `Code.gs`.
3. Open `crm/google-apps-script.js` from this repo, copy its full contents,
   and paste it into the Apps Script editor.
4. Click the disk/save icon (or press Ctrl/Cmd + S). Name the project
   "PrimeTurf CRM" when prompted.

## 3. Deploy as a Web App

1. Click **Deploy → New deployment**.
2. Click the gear icon beside "Select type" and choose **Web app**.
3. Configure:
   - **Execute as:** Me (your Google account)
   - **Who has access:** Anyone
4. Click **Deploy**.
5. Click **Authorize access**, choose your Google account, and click through
   the "Google hasn't verified this app" warning (it's your own script —
   click **Advanced → Go to PrimeTurf CRM (unsafe)** then **Allow**).
6. Copy the **Web app URL** shown after deployment. It looks like:
   `https://script.google.com/macros/s/XXXXXXXXXXXXXXXXXXXX/exec`

## 4. Connect the Website Form

1. Open `index.html`.
2. Find this line near the bottom, inside the `<script>` block:
   ```js
   const CRM_SCRIPT_URL = 'PASTE_YOUR_GOOGLE_APPS_SCRIPT_WEB_APP_URL_HERE';
   ```
3. Replace the placeholder string with the Web app URL copied in step 3.6.
4. Commit and push the change (or upload the updated `index.html` via GitHub).

## 5. Test It

1. Visit the live site, scroll to the contact form, and submit a test enquiry
   (use a real phone/email so you can confirm the round trip).
2. Confirm:
   - A new row appears in the **Leads** sheet with **Status = New**
   - A notification email arrives at **leonve33@gmail.com**
3. If nothing arrives, re-check the `CRM_SCRIPT_URL` value and that the
   deployment's "Who has access" is set to **Anyone**.

## 6. Managing Leads

Track progress using the **Status** column:

`New → Contacted → Follow Up → Proposal Sent → Closed`

Use **Notes** for context and **Follow-up Date** to set reminders — you can
sort or filter the sheet by any column to manage your pipeline.

## Updating the Script Later

Apps Script keeps the live Web app URL pinned to a specific deployment.
If you ever edit `google-apps-script.js`, you must create a **new version**
for changes to take effect:

**Deploy → Manage deployments → (pencil/edit icon) → Version: New version → Deploy**

The Web app URL stays the same, so no change is needed in `index.html`.
