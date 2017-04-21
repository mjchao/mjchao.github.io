"use strict";

var FADED_OPACITY = 0.05;

var HIDDEN = 0;
var VISIBLE = 1;
var FADED = 2;
var FADE_DURATION_RELAXED = 1250;
var FADE_DURATION_QUICK = 500;

var panel_manager = {
	menu_state: HIDDEN,
	projects_state: HIDDEN,
	skills_state: HIDDEN,
	about_state: HIDDEN,

	Init: function() {
		this.menu_panel = $("#pnl_menu");
		this.projects_panel = $("#pnl_projects");
		this.skills_panel = $("#pnl_skills");
		this.about_panel = $("#pnl_about");

		this.menu_panel.hide();
		this.projects_panel.hide();
		this.skills_panel.hide();
		this.about_panel.hide();
                this.about_panel.hide();
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
                document.title = "Mickey Chao"
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
                document.title = "Mickey Chao - Projects"
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
                document.title = "Mickey Chao - Skills"
	},

	HideSkills: function() {
		if (this.skills_state == VISIBLE) {
			this.skills_panel.fadeOut(FADE_DURATION_RELAXED);
		}
		this.skills_state = HIDDEN;
	},

	ShowAbout: function() {
		if (this.about_state == HIDDEN) {
			this.about_panel.fadeIn(FADE_DURATION_RELAXED);
		}
		this.about_state = VISIBLE;
                document.title = "Mickey Chao - About Me"
	},

	HideAbout: function() {
		if (this.about_state == VISIBLE) {
			this.about_panel.fadeOut(FADE_DURATION_RELAXED);
		}
		this.about_state = HIDDEN;
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

function ShowAbout() {
	panel_manager.FadeMenu();
	panel_manager.ShowAbout();
}

function HideAbout() {
	panel_manager.HideAbout();
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
	// If the list is fading, the user can still click the buttons.
	// We don't want to do anything in that case.
	if (panel_manager.projects_state == HIDDEN) {
		return;
	}
	if (projects_panel_manager.list_state == HIDDEN) {
		return;
	}
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
		this.skill_description = $("#skill_description");

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

	ShowDescription: function(skill) {
		this.skill_description.load(skill);
		if (this.description_state == HIDDEN) {
			this.description_panel.fadeIn(FADE_DURATION_QUICK);
			this.list_panel.fadeOut(FADE_DURATION_QUICK);
		}
		this.description_state = VISIBLE;
		this.list_state = HIDDEN;
	},
};

function ShowSkillDescription(skill) {
	if (panel_manager.skills_state == HIDDEN) {
		return;
	}
	if (skills_panel_manager.list_state == HIDDEN ) {
		return;
	}
	skills_panel_manager.ShowDescription(skill);
}

function ShowSkillsList() {
	skills_panel_manager.ShowList();
}

function InitManagers() {
	projects_panel_manager.Init();
	skills_panel_manager.Init();
	panel_manager.Init();
	document.body.style.visibility = "visible";
}

function TestAPNGSupport() {
    if (!APNG) {
        $("#img_mjchao").attr('src', 'images/mjchao.png')
        console.log("Changing image to non animated.");
    }
}

function OnLoad() {
    TestAPNGSupport();
}

window.onload = OnLoad;
