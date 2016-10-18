"use strict";
var FADED_OPACITY = 0.1;

var HIDDEN = 0;
var VISIBLE = 1;
var FADED = 2;
var FADE_DURATION_RELAXED = 1250;
var FADE_DURATION_QUICK = 500;

var panel_manager = {
	menu_state: HIDDEN,
	projects_state: HIDDEN,
	skills_state: HIDDEN,
	timeline_state: HIDDEN,

	Init: function() {
		this.menu_panel = $("#pnl_menu");
		this.projects_panel = $("#pnl_projects");
		this.skills_panel = $("#pnl_skills");
		this.timeline_panel = $("#pnl_timeline");

		this.menu_panel.hide();
		this.projects_panel.hide();
		this.skills_panel.hide();
		this.timeline_panel.hide();
		this.ShowMenu();
	},

	ShowMenu: function() {
		if (this.menu_state == HIDDEN) {
			this.menu_panel.fadeIn(FADE_DURATION_RELAXED);
		}
		else if (this.menu_state == FADED) {
			this.menu_panel.fadeTo(FADE_DURATION_RELAXED, 1.0);
		}
		this.menu_state = VISIBLE;
	},

	FadeMenu: function() {
		if (this.menu_state == VISIBLE) {
			this.menu_panel.fadeTo(FADE_DURATION_RELAXED, FADED_OPACITY);
		}
		this.menu_state = FADED;
	},

	ShowProjects: function() {
		if (this.projects_state == HIDDEN) {
			this.projects_panel.fadeIn(FADE_DURATION_RELAXED);
		}
		this.projects_state = VISIBLE;
	},

	HideProjects: function() {
		if (this.projects_state == VISIBLE) {
			this.projects_panel.fadeOut(FADE_DURATION_RELAXED);
		}
		this.projects_state = HIDDEN;
	},

	ShowSkills: function() {
		if (this.skills_state == HIDDEN) {
			this.skills_panel.fadeIn(FADE_DURATION_RELAXED);
		}
		this.skills_state = VISIBLE;
	},

	HideSkills: function() {
		if (this.skills_state == VISIBLE) {
			this.skills_panel.fadeOut(FADE_DURATION_RELAXED);
		}
		this.skills_state = HIDDEN;
	},

	ShowTimeline: function() {
		if (this.timeline_state == HIDDEN) {
			this.timeline_panel.fadeIn(FADE_DURATION);
		}
		this.timeline_state = VISIBLE;
	},

	HideTimeline: function() {
		if (this.timeline_state == VISIBLE) {
			this.timeline_panel.fadeOut(FADE_DURATION_RELAXED);
		}
		this.timeline_state = HIDDEN;
	},
	
};

function ShowMenu() {
	panel_manager.ShowMenu();
}

function ShowProjects() {
	panel_manager.FadeMenu();
	panel_manager.ShowProjects();
}

function HideProjects() {
	panel_manager.HideProjects();
	panel_manager.ShowMenu();
}

function ShowSkills() {
	panel_manager.FadeMenu();
	panel_manager.ShowSkills();
}

function HideSkills() {
	panel_manager.HideSkills();
	panel_manager.ShowMenu();
}

function ShowTimeline() {
	panel_manager.FadeMenu();
	panel_manager.ShowTimeline();
}

function HideTimeline() {
	panel_manager.HideTimeline();
	panel_manager.ShowMenu();
}

var projects_panel_manager = {
	list_state: VISIBLE,
	description_state: HIDDEN,

	Init: function() {
		this.list_panel = $("#pnl_projects_list");
		this.description_panel = $("#pnl_projects_description");
		this.project_description = $("#project_description");

		this.description_panel.hide();
	},

	ShowList: function() {
		if (this.list_state == HIDDEN) {
			this.list_panel.fadeIn(FADE_DURATION_QUICK);
			this.description_panel.fadeOut(FADE_DURATION_QUICK);
		}
		this.list_state = VISIBLE;
		this.description_state = HIDDEN;
	},

	ShowDescription: function(project) {
		this.project_description.load(project);
		if (this.description_state == HIDDEN) {
			this.description_panel.fadeIn(FADE_DURATION_QUICK);
			this.list_panel.fadeOut(FADE_DURATION_QUICK);
		}
		this.description_state = VISIBLE;
		this.list_state = HIDDEN;
	},
};

function ShowProjectDescription(project) {
	projects_panel_manager.ShowDescription(project);
}

function ShowProjectsList() {
	projects_panel_manager.ShowList();
}

var skills_panel_manager = {
	list_state: VISIBLE,
	description_state: HIDDEN,

	Init: function() {
		this.list_panel = $("#pnl_skills_list");
		this.description_panel = $("#pnl_skills_description");
		this.project_description = $("#skill_description");

		this.description_panel.hide();
	},

	ShowList: function() {
		if (this.list_state == HIDDEN) {
			this.list_panel.fadeIn(FADE_DURATION_QUICK);
			this.description_panel.fadeOut(FADE_DURATION_QUICK);
		}
		this.list_state = VISIBLE;
		this.description_state = HIDDEN;
	},

	ShowDescription: function(project) {
		this.project_description.load(project);
		if (this.description_state == HIDDEN) {
			this.description_panel.fadeIn(FADE_DURATION_QUICK);
			this.list_panel.fadeOut(FADE_DURATION_QUICK);
		}
		this.description_state = VISIBLE;
		this.list_state = HIDDEN;
	},
};

function ShowSkillsDescription(skill) {
	skills_panel_manager.ShowDescription(skill);
}

function ShowSkillsList() {
	skills_panel_manager.ShowList();
}

function InitManagers() {
	panel_manager.Init();
	projects_panel_manager.Init();
	skills_panel_manager.Init();
}
