/**
 * PrimeTurf Lead CRM — Google Apps Script
 *
 * Receives contact-form submissions from primeturf.co.za, appends each
 * enquiry as a new row in the "Leads" sheet, and emails a notification
 * to the team inbox.
 *
 * Setup instructions: see crm/SETUP_GUIDE.md in this repo.
 */

const NOTIFY_EMAIL = 'leonve33@gmail.com';
const SHEET_NAME = 'Leads';

function doPost(e) {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
    const data = e.parameter;
    const timestamp = new Date();

    sheet.appendRow([
      timestamp,
      data.full_name || '',
      data.phone || '',
      data.email || '',
      data.area || '',
      data.project_type || '',
      data.message || '',
      'New',   // Status
      '',      // Notes
      ''       // Follow-up Date
    ]);

    sendNotificationEmail(data, timestamp);

    return jsonResponse({ result: 'success' });
  } catch (err) {
    return jsonResponse({ result: 'error', error: err.message });
  }
}

function sendNotificationEmail(data, timestamp) {
  const subject = 'New PrimeTurf Enquiry — ' + (data.full_name || 'Website Lead');
  const body =
    'A new enquiry was submitted on primeturf.co.za:\n\n' +
    'Name: '            + (data.full_name    || '-') + '\n' +
    'Phone: '           + (data.phone        || '-') + '\n' +
    'Email: '           + (data.email        || '-') + '\n' +
    'Estate / Area: '   + (data.area         || '-') + '\n' +
    'Project Type: '    + (data.project_type || '-') + '\n' +
    'Heard about us via: ' + (data.referral  || '-') + '\n\n' +
    'Message:\n' + (data.message || '-') + '\n\n' +
    'Received: ' + timestamp.toLocaleString('en-ZA', { timeZone: 'Africa/Johannesburg' });

  MailApp.sendEmail(NOTIFY_EMAIL, subject, body);
}

function jsonResponse(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
