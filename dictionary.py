# country_capital = {
#     "pakistan" : "Islamabad",
#     "India"    : "Dehli",
#     "Afghanistan" : "Qabul",
# }
# print(country_capital)
# print(type(country_capital))
# country_capital["IRAN"] = "Tahran" 
# print(country_capital)
# print(country_capital["India"])
# print(country_capital["IRAN"])
# for cap in country_capital:
#     print(cap)
#!/usr/bin/env python3
"""
Police Department Duty Chart Management System
=============================================
3 Shifts: Morning (8AM-3PM), Evening (3PM-11PM), Night (11PM-6AM)
Morning: 6-7 Officers with 6 rotating duty points (1-hour rotation)
Evening: 4 Officers
Night: 4 Officers
Tracks absences (Off / Absent)
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
from datetime import datetime, date, timedelta
from collections import defaultdict

# ─────────────────────── CONSTANTS ───────────────────────
SHIFTS = {
    "Morning": {"start": "08:00", "end": "15:00", "color": "#FFF3CD", "header": "#F59E0B"},
    "Evening": {"start": "15:00", "end": "23:00", "color": "#D1ECF1", "header": "#0EA5E9"},
    "Night":   {"start": "23:00", "end": "06:00", "color": "#D6D3F0", "header": "#6D28D9"},
}

MORNING_POINTS = [
    "Gate / Main Entry",
    "Patrol Zone A",
    "Patrol Zone B",
    "Control Room",
    "Investigation Unit",
    "Perimeter Watch",
]

POINT_HOURS = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00"]

DATA_FILE = "police_duty_data.json"
RANKS = ["Constable", "Head Constable", "ASI", "SI", "Inspector", "DSP"]


# ─────────────────────── DATA LAYER ───────────────────────
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return {"officers": [], "schedules": {}, "absences": {}}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


# ─────────────────────── MAIN APP ───────────────────────
class PoliceDutyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Police Department — Duty Chart System")
        self.root.geometry("1280x820")
        self.root.configure(bg="#1E293B")
        self.root.minsize(1100, 700)

        self.data = load_data()
        self.selected_date = date.today()

        self._build_ui()
        self._refresh_all()

    # ── UI SKELETON ──────────────────────────────────────
    def _build_ui(self):
        # Header bar
        hdr = tk.Frame(self.root, bg="#0F172A", height=60)
        hdr.pack(fill="x")
        tk.Label(hdr, text="🚔  Police Department — Duty Chart", font=("Helvetica", 18, "bold"),
                 bg="#0F172A", fg="white").pack(side="left", padx=20, pady=12)
        tk.Label(hdr, text="Pakistan Police", font=("Helvetica", 11),
                 bg="#0F172A", fg="#94A3B8").pack(side="right", padx=20)

        # Toolbar
        tb = tk.Frame(self.root, bg="#1E293B", pady=6)
        tb.pack(fill="x")
        self._toolbar(tb)

        # Main notebook
        self.nb = ttk.Notebook(self.root)
        self.nb.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TNotebook", background="#1E293B", borderwidth=0)
        style.configure("TNotebook.Tab", background="#334155", foreground="white",
                        padding=[14, 8], font=("Helvetica", 10, "bold"))
        style.map("TNotebook.Tab", background=[("selected", "#0EA5E9")],
                  foreground=[("selected", "white")])

        # Tabs
        self.tab_chart   = tk.Frame(self.nb, bg="#F1F5F9")
        self.tab_morning = tk.Frame(self.nb, bg="#F1F5F9")
        self.tab_absence = tk.Frame(self.nb, bg="#F1F5F9")
        self.tab_officers= tk.Frame(self.nb, bg="#F1F5F9")
        self.tab_report  = tk.Frame(self.nb, bg="#F1F5F9")

        self.nb.add(self.tab_chart,   text="📋  Daily Duty Chart")
        self.nb.add(self.tab_morning, text="☀️  Morning Point Rotation")
        self.nb.add(self.tab_absence, text="❌  Absences / Off-Duty")
        self.nb.add(self.tab_officers,text="👮  Officer Management")
        self.nb.add(self.tab_report,  text="📊  Monthly Report")

        self._build_chart_tab()
        self._build_morning_tab()
        self._build_absence_tab()
        self._build_officers_tab()
        self._build_report_tab()

    def _toolbar(self, parent):
        tk.Label(parent, text="Select Date:", bg="#1E293B", fg="white",
                 font=("Helvetica", 10)).pack(side="left", padx=(14, 4))

        self.date_var = tk.StringVar(value=self.selected_date.strftime("%Y-%m-%d"))
        date_entry = tk.Entry(parent, textvariable=self.date_var, width=12,
                              font=("Courier", 11), bg="#334155", fg="white",
                              insertbackground="white", relief="flat")
        date_entry.pack(side="left")

        btn_style = dict(bg="#0EA5E9", fg="white", font=("Helvetica", 9, "bold"),
                         relief="flat", padx=10, pady=4, cursor="hand2")
        tk.Button(parent, text="Load", command=self._load_date, **btn_style).pack(side="left", padx=6)
        tk.Button(parent, text="◀ Prev", command=self._prev_day, **btn_style).pack(side="left", padx=2)
        tk.Button(parent, text="Next ▶", command=self._next_day, **btn_style).pack(side="left", padx=2)

        tk.Button(parent, text="✅  Save Schedule", command=self._save_schedule,
                  bg="#10B981", fg="white", font=("Helvetica", 9, "bold"),
                  relief="flat", padx=12, pady=4, cursor="hand2").pack(side="left", padx=14)

        self.status_var = tk.StringVar(value="")
        tk.Label(parent, textvariable=self.status_var, bg="#1E293B",
                 fg="#10B981", font=("Helvetica", 9)).pack(side="right", padx=16)

    # ── CHART TAB ────────────────────────────────────────
    def _build_chart_tab(self):
        self.chart_frame = tk.Frame(self.tab_chart, bg="#F1F5F9")
        self.chart_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def _render_chart(self):
        for w in self.chart_frame.winfo_children():
            w.destroy()

        date_str = self.selected_date.strftime("%Y-%m-%d")
        day_name = self.selected_date.strftime("%A, %d %B %Y")

        tk.Label(self.chart_frame, text=f"Duty Chart — {day_name}",
                 font=("Helvetica", 15, "bold"), bg="#F1F5F9", fg="#1E293B").pack(pady=(4, 10))

        canvas = tk.Canvas(self.chart_frame, bg="#F1F5F9", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.chart_frame, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#F1F5F9")
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        sched = self.data["schedules"].get(date_str, {})
        absences = self.data["absences"].get(date_str, {})
        officers = self.data["officers"]

        for shift_name, shift_info in SHIFTS.items():
            # Determine max officers
            max_off = 7 if shift_name == "Morning" else 4

            frame = tk.LabelFrame(scroll_frame,
                                  text=f"  {shift_name} Shift  |  {shift_info['start']} – {shift_info['end']}  |  Max: {max_off} Officers  ",
                                  font=("Helvetica", 11, "bold"),
                                  bg=shift_info["color"], fg="#1E293B",
                                  labelanchor="n", pady=8, padx=8,
                                  relief="ridge", bd=2)
            frame.pack(fill="x", padx=6, pady=6)

            headers = ["#", "Officer Name", "Badge No.", "Rank", "Duty Point", "Status"]
            col_w   = [30,  200,            100,         120,    160,           100]
            for c, (h, w) in enumerate(zip(headers, col_w)):
                tk.Label(frame, text=h, width=w//8, font=("Helvetica", 9, "bold"),
                         bg=shift_info["header"], fg="white", relief="flat",
                         anchor="center", padx=4, pady=4).grid(row=0, column=c, padx=1, pady=(0,2))

            shift_officers = sched.get(shift_name, [])
            rows_shown = max(max_off, len(shift_officers))

            for i in range(rows_shown):
                bg = "#FFFFFF" if i % 2 == 0 else shift_info["color"]
                tk.Label(frame, text=str(i+1), bg=bg, relief="flat",
                         font=("Helvetica", 9), anchor="center", width=3).grid(row=i+1, column=0, padx=1, pady=1)

                if i < len(shift_officers):
                    oid = shift_officers[i]
                    officer = next((o for o in officers if o["id"] == oid), None)
                    abs_status = absences.get(oid, "Present")
                    status_color = "#10B981" if abs_status == "Present" else "#EF4444"

                    name  = officer["name"]  if officer else f"Officer {oid}"
                    badge = officer["badge"] if officer else "—"
                    rank  = officer["rank"]  if officer else "—"
                    point = "Rotating (See Morning Tab)" if shift_name == "Morning" else "General Patrol"

                    for c, (val, w) in enumerate(zip([name, badge, rank, point], col_w[1:5])):
                        tk.Label(frame, text=val, bg=bg, relief="flat",
                                 font=("Helvetica", 9), anchor="w", padx=4, width=w//8).grid(row=i+1, column=c+1, padx=1, pady=1)
                    tk.Label(frame, text=abs_status, bg=bg, fg=status_color,
                             font=("Helvetica", 9, "bold"), anchor="center", width=12).grid(row=i+1, column=5, padx=1, pady=1)
                else:
                    for c in range(1, 6):
                        tk.Label(frame, text="—", bg=bg, fg="#94A3B8",
                                 font=("Helvetica", 9), anchor="center", width=col_w[c]//8).grid(row=i+1, column=c, padx=1, pady=1)

    # ── MORNING ROTATION TAB ─────────────────────────────
    def _build_morning_tab(self):
        self.morning_frame = tk.Frame(self.tab_morning, bg="#F1F5F9")
        self.morning_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def _render_morning(self):
        for w in self.morning_frame.winfo_children():
            w.destroy()

        date_str = self.selected_date.strftime("%Y-%m-%d")
        officers_on_morning = self.data["schedules"].get(date_str, {}).get("Morning", [])
        officers = self.data["officers"]

        tk.Label(self.morning_frame,
                 text="☀️  Morning Shift — Hourly Point Rotation (08:00 – 15:00)",
                 font=("Helvetica", 14, "bold"), bg="#F1F5F9", fg="#1E293B").pack(pady=(4, 10))

        tk.Label(self.morning_frame,
                 text="Each officer rotates to the next point every hour. Point assignments are auto-calculated.",
                 font=("Helvetica", 9), bg="#F1F5F9", fg="#64748B").pack()

        if not officers_on_morning:
            tk.Label(self.morning_frame,
                     text="⚠  No officers assigned to Morning shift for this date.\nGo to Daily Duty Chart and assign officers first.",
                     font=("Helvetica", 11), bg="#FEF3C7", fg="#92400E",
                     relief="flat", padx=20, pady=20).pack(pady=30)
            return

        # Build rotation grid
        container = tk.Frame(self.morning_frame, bg="#F1F5F9")
        container.pack(fill="both", expand=True, pady=10, padx=6)

        # Canvas + scroll
        canvas = tk.Canvas(container, bg="#F1F5F9", highlightthickness=0)
        h_scroll = ttk.Scrollbar(container, orient="horizontal", command=canvas.xview)
        v_scroll = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        inner = tk.Frame(canvas, bg="#F1F5F9")
        inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=inner, anchor="nw")
        canvas.configure(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)
        canvas.pack(side="left", fill="both", expand=True)
        v_scroll.pack(side="right", fill="y")
        h_scroll.pack(side="bottom", fill="x")

        # Header row (hours)
        tk.Label(inner, text="Point \\ Hour", bg="#0F172A", fg="white",
                 font=("Helvetica", 9, "bold"), width=22, pady=6, anchor="center").grid(row=0, column=0, padx=1, pady=1)
        for c, hr in enumerate(POINT_HOURS):
            tk.Label(inner, text=hr, bg="#F59E0B", fg="white",
                     font=("Helvetica", 9, "bold"), width=16, pady=6, anchor="center").grid(row=0, column=c+1, padx=1, pady=1)

        n_officers = len(officers_on_morning)
        n_points   = len(MORNING_POINTS)

        for r, point in enumerate(MORNING_POINTS):
            bg_row = "#FFFBEB" if r % 2 == 0 else "#FEF3C7"
            tk.Label(inner, text=point, bg="#92400E", fg="white",
                     font=("Helvetica", 9, "bold"), width=22, anchor="w",
                     padx=6, pady=5).grid(row=r+1, column=0, padx=1, pady=1)

            for c in range(len(POINT_HOURS)):
                # Rotate officers across points each hour
                officer_idx = (r + c) % n_officers
                oid = officers_on_morning[officer_idx]
                officer = next((o for o in officers if o["id"] == oid), None)
                name = officer["name"] if officer else f"ID:{oid}"
                badge = officer["badge"] if officer else ""

                cell = tk.Frame(inner, bg=bg_row, relief="flat", bd=1)
                cell.grid(row=r+1, column=c+1, padx=1, pady=1, sticky="nsew")
                tk.Label(cell, text=name, bg=bg_row, fg="#1E293B",
                         font=("Helvetica", 9, "bold"), width=14, anchor="center").pack()
                tk.Label(cell, text=badge, bg=bg_row, fg="#64748B",
                         font=("Helvetica", 8), width=14, anchor="center").pack()

        # Legend
        leg = tk.Frame(self.morning_frame, bg="#E0F2FE", pady=8)
        leg.pack(fill="x", padx=6, pady=(6, 0))
        tk.Label(leg, text="ℹ  Rotation Rule: Officer assigned to Point 1 at 8AM moves to Point 2 at 9AM, Point 3 at 10AM … and wraps back.",
                 bg="#E0F2FE", fg="#0369A1", font=("Helvetica", 9)).pack()

    # ── ABSENCE TAB ───────────────────────────────────────
    def _build_absence_tab(self):
        top = tk.Frame(self.tab_absence, bg="#F1F5F9")
        top.pack(fill="x", padx=12, pady=10)
        tk.Label(top, text="Absence & Off-Duty Management",
                 font=("Helvetica", 14, "bold"), bg="#F1F5F9").pack(side="left")
        tk.Button(top, text="➕ Mark Absence", command=self._mark_absence,
                  bg="#EF4444", fg="white", font=("Helvetica", 9, "bold"),
                  relief="flat", padx=10, pady=4, cursor="hand2").pack(side="right")
        tk.Button(top, text="✅ Mark Present", command=self._mark_present,
                  bg="#10B981", fg="white", font=("Helvetica", 9, "bold"),
                  relief="flat", padx=10, pady=4, cursor="hand2").pack(side="right", padx=8)

        cols = ("Date", "Officer", "Badge", "Shift", "Status", "Reason")
        self.abs_tree = ttk.Treeview(self.tab_absence, columns=cols, show="headings", height=20)
        widths = [100, 180, 90, 90, 90, 250]
        for col, w in zip(cols, widths):
            self.abs_tree.heading(col, text=col)
            self.abs_tree.column(col, width=w, anchor="center")

        style = ttk.Style()
        style.configure("Treeview", rowheight=26, font=("Helvetica", 9))
        style.configure("Treeview.Heading", font=("Helvetica", 9, "bold"))
        self.abs_tree.tag_configure("absent", background="#FEE2E2")
        self.abs_tree.tag_configure("off",    background="#FEF3C7")

        sb = ttk.Scrollbar(self.tab_absence, orient="vertical", command=self.abs_tree.yview)
        self.abs_tree.configure(yscrollcommand=sb.set)
        self.abs_tree.pack(fill="both", expand=True, padx=12, pady=(0,10), side="left")
        sb.pack(side="right", fill="y", pady=(50,10))

    def _render_absence(self):
        for row in self.abs_tree.get_children():
            self.abs_tree.delete(row)
        officers = {o["id"]: o for o in self.data["officers"]}
        for date_str, abs_dict in sorted(self.data["absences"].items()):
            for oid, status_info in abs_dict.items():
                if isinstance(status_info, dict):
                    status = status_info.get("status", "Absent")
                    reason = status_info.get("reason", "")
                    shift  = status_info.get("shift", "—")
                else:
                    status = status_info
                    reason = ""
                    shift  = "—"
                o = officers.get(oid, {})
                tag = "absent" if status == "Absent" else "off"
                self.abs_tree.insert("", "end", values=(
                    date_str, o.get("name", oid), o.get("badge", "—"),
                    shift, status, reason
                ), tags=(tag,))

    def _mark_absence(self):
        self._absence_dialog("Absent")

    def _mark_present(self):
        # Remove absence for selected
        sel = self.abs_tree.selection()
        if not sel:
            messagebox.showinfo("Select Row", "Please select an absence record to mark as present.")
            return
        # For simplicity: remove entry
        vals = self.abs_tree.item(sel[0], "values")
        date_str, _, badge = vals[0], vals[1], vals[2]
        officer = next((o for o in self.data["officers"] if o["badge"] == badge), None)
        if officer and date_str in self.data["absences"]:
            self.data["absences"][date_str].pop(officer["id"], None)
            save_data(self.data)
            self._refresh_all()
            self.status_var.set("✅ Marked as Present")

    def _absence_dialog(self, default_status):
        dlg = tk.Toplevel(self.root)
        dlg.title("Record Absence / Off-Duty")
        dlg.geometry("400x380")
        dlg.configure(bg="#F1F5F9")
        dlg.grab_set()

        officers = self.data["officers"]
        if not officers:
            messagebox.showwarning("No Officers", "Add officers first.")
            dlg.destroy()
            return

        tk.Label(dlg, text="Record Absence or Off-Duty", font=("Helvetica", 12, "bold"),
                 bg="#F1F5F9").pack(pady=12)

        fields = tk.Frame(dlg, bg="#F1F5F9")
        fields.pack(padx=20, fill="x")

        # Date
        tk.Label(fields, text="Date:", bg="#F1F5F9", font=("Helvetica", 10)).grid(row=0, column=0, sticky="w", pady=5)
        date_var = tk.StringVar(value=self.selected_date.strftime("%Y-%m-%d"))
        tk.Entry(fields, textvariable=date_var, width=14).grid(row=0, column=1, sticky="w", padx=8)

        # Officer
        tk.Label(fields, text="Officer:", bg="#F1F5F9", font=("Helvetica", 10)).grid(row=1, column=0, sticky="w", pady=5)
        officer_names = [f"{o['name']} ({o['badge']})" for o in officers]
        officer_var = tk.StringVar()
        ttk.Combobox(fields, textvariable=officer_var, values=officer_names, width=22).grid(row=1, column=1, sticky="w", padx=8)

        # Shift
        tk.Label(fields, text="Shift:", bg="#F1F5F9", font=("Helvetica", 10)).grid(row=2, column=0, sticky="w", pady=5)
        shift_var = tk.StringVar(value="Morning")
        ttk.Combobox(fields, textvariable=shift_var, values=list(SHIFTS.keys()), width=14).grid(row=2, column=1, sticky="w", padx=8)

        # Status
        tk.Label(fields, text="Status:", bg="#F1F5F9", font=("Helvetica", 10)).grid(row=3, column=0, sticky="w", pady=5)
        status_var = tk.StringVar(value=default_status)
        ttk.Combobox(fields, textvariable=status_var, values=["Absent", "Off-Duty", "Sick Leave", "Emergency Leave"],
                     width=16).grid(row=3, column=1, sticky="w", padx=8)

        # Reason
        tk.Label(fields, text="Reason:", bg="#F1F5F9", font=("Helvetica", 10)).grid(row=4, column=0, sticky="w", pady=5)
        reason_var = tk.StringVar()
        tk.Entry(fields, textvariable=reason_var, width=22).grid(row=4, column=1, sticky="w", padx=8)

        def save():
            try:
                sel_officer = officers[officer_names.index(officer_var.get())]
            except (ValueError, IndexError):
                messagebox.showerror("Error", "Select a valid officer.")
                return
            d = date_var.get()
            if d not in self.data["absences"]:
                self.data["absences"][d] = {}
            self.data["absences"][d][sel_officer["id"]] = {
                "status": status_var.get(),
                "shift": shift_var.get(),
                "reason": reason_var.get()
            }
            save_data(self.data)
            self._refresh_all()
            self.status_var.set(f"✅ Absence recorded for {sel_officer['name']}")
            dlg.destroy()

        tk.Button(dlg, text="Save Record", command=save,
                  bg="#EF4444", fg="white", font=("Helvetica", 10, "bold"),
                  relief="flat", padx=16, pady=6, cursor="hand2").pack(pady=20)

    # ── OFFICERS TAB ─────────────────────────────────────
    def _build_officers_tab(self):
        top = tk.Frame(self.tab_officers, bg="#F1F5F9")
        top.pack(fill="x", padx=12, pady=10)
        tk.Label(top, text="Officer Management", font=("Helvetica", 14, "bold"),
                 bg="#F1F5F9").pack(side="left")
        tk.Button(top, text="➕ Add Officer", command=self._add_officer,
                  bg="#0EA5E9", fg="white", font=("Helvetica", 9, "bold"),
                  relief="flat", padx=10, pady=4, cursor="hand2").pack(side="right")
        tk.Button(top, text="🗑 Remove", command=self._remove_officer,
                  bg="#EF4444", fg="white", font=("Helvetica", 9, "bold"),
                  relief="flat", padx=10, pady=4, cursor="hand2").pack(side="right", padx=8)

        cols = ("ID", "Name", "Badge No.", "Rank", "Contact", "Assigned Shift")
        self.off_tree = ttk.Treeview(self.tab_officers, columns=cols, show="headings", height=22)
        widths = [50, 180, 100, 120, 130, 130]
        for col, w in zip(cols, widths):
            self.off_tree.heading(col, text=col)
            self.off_tree.column(col, width=w, anchor="center")
        self.off_tree.pack(fill="both", expand=True, padx=12, pady=(0,10))

        # Shift assignment panel
        assign_frame = tk.LabelFrame(self.tab_officers, text="  Quick Shift Assignment  ",
                                     bg="#F1F5F9", font=("Helvetica", 10, "bold"), padx=10, pady=8)
        assign_frame.pack(fill="x", padx=12, pady=(0, 10))

        tk.Label(assign_frame, text="Date:", bg="#F1F5F9").pack(side="left")
        self.assign_date_var = tk.StringVar(value=self.selected_date.strftime("%Y-%m-%d"))
        tk.Entry(assign_frame, textvariable=self.assign_date_var, width=12).pack(side="left", padx=6)

        tk.Label(assign_frame, text="Shift:", bg="#F1F5F9").pack(side="left", padx=(10, 2))
        self.assign_shift_var = tk.StringVar(value="Morning")
        ttk.Combobox(assign_frame, textvariable=self.assign_shift_var,
                     values=list(SHIFTS.keys()), width=10).pack(side="left")

        tk.Button(assign_frame, text="Assign Selected Officer to Shift",
                  command=self._quick_assign,
                  bg="#10B981", fg="white", font=("Helvetica", 9, "bold"),
                  relief="flat", padx=10, pady=3, cursor="hand2").pack(side="left", padx=14)

    def _render_officers(self):
        for row in self.off_tree.get_children():
            self.off_tree.delete(row)
        # Compute current assignments
        date_str = self.selected_date.strftime("%Y-%m-%d")
        sched = self.data["schedules"].get(date_str, {})
        assigned = {}
        for shift, oids in sched.items():
            for oid in oids:
                assigned[oid] = shift

        for o in self.data["officers"]:
            self.off_tree.insert("", "end", values=(
                o["id"], o["name"], o["badge"], o["rank"],
                o.get("contact", "—"), assigned.get(o["id"], "Unassigned")
            ))

    def _add_officer(self):
        dlg = tk.Toplevel(self.root)
        dlg.title("Add New Officer")
        dlg.geometry("380x320")
        dlg.configure(bg="#F1F5F9")
        dlg.grab_set()

        tk.Label(dlg, text="Add New Officer", font=("Helvetica", 12, "bold"),
                 bg="#F1F5F9").pack(pady=12)

        frame = tk.Frame(dlg, bg="#F1F5F9")
        frame.pack(padx=20, fill="x")

        labels = ["Full Name:", "Badge No.:", "Rank:", "Contact:"]
        vars_   = [tk.StringVar() for _ in labels]
        for i, (lbl, var) in enumerate(zip(labels, vars_)):
            tk.Label(frame, text=lbl, bg="#F1F5F9", width=12, anchor="w").grid(row=i, column=0, pady=6)
            if lbl == "Rank:":
                ttk.Combobox(frame, textvariable=var, values=RANKS, width=18).grid(row=i, column=1, sticky="w")
                var.set(RANKS[0])
            else:
                tk.Entry(frame, textvariable=var, width=20).grid(row=i, column=1, sticky="w")

        def save():
            name, badge, rank, contact = [v.get().strip() for v in vars_]
            if not name or not badge:
                messagebox.showerror("Error", "Name and Badge are required.")
                return
            if any(o["badge"] == badge for o in self.data["officers"]):
                messagebox.showerror("Error", "Badge number already exists.")
                return
            new_id = f"off_{len(self.data['officers'])+1:04d}"
            self.data["officers"].append({
                "id": new_id, "name": name, "badge": badge,
                "rank": rank, "contact": contact
            })
            save_data(self.data)
            self._refresh_all()
            self.status_var.set(f"✅ Officer {name} added")
            dlg.destroy()

        tk.Button(dlg, text="Add Officer", command=save,
                  bg="#0EA5E9", fg="white", font=("Helvetica", 10, "bold"),
                  relief="flat", padx=16, pady=6, cursor="hand2").pack(pady=20)

    def _remove_officer(self):
        sel = self.off_tree.selection()
        if not sel:
            messagebox.showinfo("Select", "Select an officer to remove.")
            return
        vals = self.off_tree.item(sel[0], "values")
        oid = vals[0]
        if messagebox.askyesno("Confirm", f"Remove officer: {vals[1]}?"):
            self.data["officers"] = [o for o in self.data["officers"] if o["id"] != oid]
            save_data(self.data)
            self._refresh_all()

    def _quick_assign(self):
        sel = self.off_tree.selection()
        if not sel:
            messagebox.showinfo("Select", "Select an officer first.")
            return
        oid = self.off_tree.item(sel[0], "values")[0]
        d = self.assign_date_var.get()
        shift = self.assign_shift_var.get()
        if d not in self.data["schedules"]:
            self.data["schedules"][d] = {}
        if shift not in self.data["schedules"][d]:
            self.data["schedules"][d][shift] = []

        # Capacity check
        max_off = 7 if shift == "Morning" else 4
        existing = self.data["schedules"][d][shift]
        if oid in existing:
            messagebox.showinfo("Already Assigned", "This officer is already in this shift.")
            return
        if len(existing) >= max_off:
            messagebox.showwarning("Shift Full", f"{shift} shift is at maximum capacity ({max_off}).")
            return

        # Remove from other shifts same day
        for s in SHIFTS:
            if s != shift and oid in self.data["schedules"].get(d, {}).get(s, []):
                self.data["schedules"][d][s].remove(oid)

        self.data["schedules"][d][shift].append(oid)
        save_data(self.data)
        self._refresh_all()
        self.status_var.set(f"✅ Assigned to {shift}")

    # ── REPORT TAB ────────────────────────────────────────
    def _build_report_tab(self):
        top = tk.Frame(self.tab_report, bg="#F1F5F9")
        top.pack(fill="x", padx=12, pady=10)
        tk.Label(top, text="Monthly Summary Report", font=("Helvetica", 14, "bold"),
                 bg="#F1F5F9").pack(side="left")

        tk.Label(top, text="Month (YYYY-MM):", bg="#F1F5F9").pack(side="left", padx=(20, 4))
        self.report_month_var = tk.StringVar(value=date.today().strftime("%Y-%m"))
        tk.Entry(top, textvariable=self.report_month_var, width=10).pack(side="left")
        tk.Button(top, text="Generate", command=self._generate_report,
                  bg="#6D28D9", fg="white", font=("Helvetica", 9, "bold"),
                  relief="flat", padx=10, pady=3, cursor="hand2").pack(side="left", padx=8)

        self.report_text = tk.Text(self.tab_report, font=("Courier", 9),
                                   bg="#0F172A", fg="#E2E8F0", relief="flat",
                                   padx=14, pady=10, state="disabled")
        self.report_text.pack(fill="both", expand=True, padx=12, pady=(0, 12))

    def _generate_report(self):
        month_str = self.report_month_var.get()
        try:
            year, month = map(int, month_str.split("-"))
        except ValueError:
            messagebox.showerror("Error", "Enter month as YYYY-MM")
            return

        officers = {o["id"]: o for o in self.data["officers"]}
        duty_count   = defaultdict(lambda: defaultdict(int))  # officer -> shift -> count
        absence_count= defaultdict(int)

        for date_str, sched in self.data["schedules"].items():
            if not date_str.startswith(month_str):
                continue
            for shift, oids in sched.items():
                for oid in oids:
                    duty_count[oid][shift] += 1

        for date_str, abs_dict in self.data["absences"].items():
            if not date_str.startswith(month_str):
                continue
            for oid in abs_dict:
                absence_count[oid] += 1

        lines = []
        lines.append(f"{'='*70}")
        lines.append(f"  POLICE DEPARTMENT — MONTHLY DUTY REPORT")
        lines.append(f"  Period: {month_str}")
        lines.append(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        lines.append(f"{'='*70}")
        lines.append(f"{'Officer':<22} {'Badge':<10} {'Rank':<14} {'Morn':>5} {'Eve':>5} {'Night':>6} {'Total':>6} {'Absences':>9}")
        lines.append(f"{'-'*70}")

        for oid, o in officers.items():
            m = duty_count[oid].get("Morning", 0)
            e = duty_count[oid].get("Evening", 0)
            n = duty_count[oid].get("Night", 0)
            t = m + e + n
            a = absence_count[oid]
            lines.append(f"{o['name']:<22} {o['badge']:<10} {o['rank']:<14} {m:>5} {e:>5} {n:>6} {t:>6} {a:>9}")

        lines.append(f"{'='*70}")

        self.report_text.configure(state="normal")
        self.report_text.delete("1.0", "end")
        self.report_text.insert("end", "\n".join(lines))
        self.report_text.configure(state="disabled")

    # ── SAVE SCHEDULE ─────────────────────────────────────
    def _save_schedule(self):
        save_data(self.data)
        self.status_var.set(f"✅ Saved — {self.selected_date.strftime('%Y-%m-%d')}")

    # ── DATE NAVIGATION ───────────────────────────────────
    def _load_date(self):
        try:
            self.selected_date = date.fromisoformat(self.date_var.get())
            self._refresh_all()
        except ValueError:
            messagebox.showerror("Error", "Invalid date. Use YYYY-MM-DD format.")

    def _prev_day(self):
        self.selected_date -= timedelta(days=1)
        self.date_var.set(self.selected_date.strftime("%Y-%m-%d"))
        self._refresh_all()

    def _next_day(self):
        self.selected_date += timedelta(days=1)
        self.date_var.set(self.selected_date.strftime("%Y-%m-%d"))
        self._refresh_all()

    def _refresh_all(self):
        self.date_var.set(self.selected_date.strftime("%Y-%m-%d"))
        self._render_chart()
        self._render_morning()
        self._render_absence()
        self._render_officers()


# ─────────────────────── ENTRY POINT ───────────────────────
def main():
    root = tk.Tk()
    try:
        root.iconbitmap("")
    except Exception:
        pass
    app = PoliceDutyApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()