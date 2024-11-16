NAME   = ディスクゴルフ大会のための競技マニュアル
TARGET = $(NAME)

PANDOC = pandoc

CONFIGDIR = config
TEMPLATEDIR = templates
FILTERSDIR = filters
SOURCEDIR = ../source
MARKDOWNDIR = markdown
LOCAL_SOURCEDIR = sources

COVER_DATA = cover.tex
BACKCOVER_DATA = backcover.tex
TEMPLATE = $(TEMPLATEDIR)/main.tex
COVER_TEMPLATE = $(TEMPLATEDIR)/cover-template.tex
BACKCOVER_TEMPLATE = $(TEMPLATEDIR)/backcover-template.tex
SOURCE = \
	$(LOCAL_SOURCEDIR)/preface.md \
	$(LOCAL_SOURCEDIR)/newpage.md \
	$(SOURCEDIR)/Introduction.md \
	$(LOCAL_SOURCEDIR)/newpage.md \
	$(SOURCEDIR)/Section1TournamentProcedures.md \
	$(SOURCEDIR)/1.01PlayerEligibility.md \
	$(SOURCEDIR)/1.02TournamentRegistration.md \
	$(SOURCEDIR)/1.03WithdrawalsAndRefunds.md \
	$(SOURCEDIR)/1.04EventCheckIn.md \
	$(SOURCEDIR)/1.05PracticeRoundsBeginningPlayLateArrivals.md \
	$(SOURCEDIR)/1.06GroupingAndSectioning.md \
	$(SOURCEDIR)/1.07SuspensionOfPlay.md \
	$(SOURCEDIR)/1.08ReductionOfFieldSize.md \
	$(SOURCEDIR)/1.09Ties.md \
	$(SOURCEDIR)/1.10DistributionOfPrizes.md \
	$(SOURCEDIR)/1.11Officials.md \
	$(SOURCEDIR)/1.12TournamentOfficials.md \
	$(SOURCEDIR)/1.13YouthSafety.md \
	$(SOURCEDIR)/1.14Leagues.md \
	$(LOCAL_SOURCEDIR)/newpage.md \
	$(SOURCEDIR)/Section2DivisionQualifications.md \
	$(SOURCEDIR)/2.01Qualifications.md \
	$(SOURCEDIR)/2.02Exceptions.md \
	$(SOURCEDIR)/2.03ReclassificationOfProfessionalAmateur.md \
	$(SOURCEDIR)/2.04ProsPlayingAmAmsPlayingPro.md \
	$(SOURCEDIR)/2.05TrueAmateur.md \
	$(LOCAL_SOURCEDIR)/newpage.md \
	$(SOURCEDIR)/Section3PlayerCodeConduct.md \
	$(SOURCEDIR)/3.01General.md \
	$(SOURCEDIR)/3.02PaceOfPlay.md \
	$(SOURCEDIR)/3.03PlayerMisconduct.md \
	$(SOURCEDIR)/3.04DressCode.md \
	$(SOURCEDIR)/3.05CartsCaddiesAndGroups.md \
	$(SOURCEDIR)/3.06TourPlayerMediaAndSponsorRelations.md \
	$(SOURCEDIR)/3.07TourVendorPolicies.md \
	$(SOURCEDIR)/3.08TournamentDirectorRightsAndResponsibilities.md \
	$(LOCAL_SOURCEDIR)/newpage.md \
	$(SOURCEDIR)/Section4MajorsEliteSeries.md \
	$(SOURCEDIR)/4.01Applicability.md \
	$(SOURCEDIR)/4.02Eligibility.md \
	$(SOURCEDIR)/4.03CaddiesAndGroups.md \
	$(SOURCEDIR)/4.04PlayerCodeOfConduct.md \
	$(SOURCEDIR)/4.05RegistrationCheckingInAndBeginningPlay.md \
	$(SOURCEDIR)/4.06Scoring.md \
	$(LOCAL_SOURCEDIR)/newpage.md \
	$(SOURCEDIR)/Section5PDGATourStandards.md \
	$(SOURCEDIR)/5.01Applicability.md \
	$(SOURCEDIR)/5.02DivisionsReclassification.md \
	$(SOURCEDIR)/5.03PreparingCourse.md \
	$(SOURCEDIR)/5.04FinancesPayout.md \
	$(SOURCEDIR)/5.05TierTargetRequirements.md \
	$(SOURCEDIR)/5.06DidNotPlay.md \
	$(SOURCEDIR)/5.07ReportingRequirements.md \
	$(SOURCEDIR)/5.08MajorEliteSeriesRequirements.md \
	$(SOURCEDIR)/5.09A-TierRequirements.md \
	$(SOURCEDIR)/5.10X-DesignatedEvents.md \
	$(LOCAL_SOURCEDIR)/newpage.md \
	$(SOURCEDIR)/Section6InternationalVariancesExceptions.md \
	$(SOURCEDIR)/6.01ApplicabilityExceptions.md \
	$(SOURCEDIR)/6.02VariancesORDG.md \
	$(SOURCEDIR)/6.03VariancesCM.md \
	$(LOCAL_SOURCEDIR)/newpage.md

$(TARGET).pdf: $(SOURCE) $(COVER_DATA) $(BACKCOVER_DATA) $(TEMPLATE)
	$(PANDOC) \
		-d $(CONFIGDIR)/filters.yaml \
		-d $(CONFIGDIR)/common.yaml \
		-d $(CONFIGDIR)/body.yaml \
		-B $(COVER_DATA) \
		-A $(BACKCOVER_DATA) \
		-o $(TARGET).pdf \
		$(SOURCE)

$(COVER_DATA) : $(COVER_TEMPLATE) $(CONFIGDIR)/common.yaml $(CONFIGDIR)/cover.yaml
	echo "" | $(PANDOC) \
		-d $(CONFIGDIR)/common.yaml \
		-d $(CONFIGDIR)/cover.yaml \
		-o $(COVER_DATA)

$(BACKCOVER_DATA) : $(BACKCOVER_TEMPLATE) $(CONFIGDIR)/common.yaml $(CONFIGDIR)/revisions.yaml $(CONFIGDIR)/backcover.yaml
	echo "" | $(PANDOC) \
		-d $(CONFIGDIR)/common.yaml \
		-d $(CONFIGDIR)/backcover.yaml \
		-d $(CONFIGDIR)/revisions.yaml \
		-o $(BACKCOVER_DATA)

all: clean $(TARGET).pdf

clean:
	rm -f $(TARGET).html $(TARGET).pdf $(COVER_DATA) $(BACKCOVER_DATA)
