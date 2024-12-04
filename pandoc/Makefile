#
# Pandocを使って、マークダウンファイルからPDFを生成する
#
TITLE = CompetitionManualForDiscGolfEvents
VERSION = 2025
TARGET = $(TITLE)-$(VERSION).pdf

PANDOC = pandoc
CONFIGDIR = config
TEMPLATEDIR = templates
FILTERSDIR = filters
SOURCEDIR = ../source
LOCAL_SOURCEDIR = sources

SOURCE = \
	$(LOCAL_SOURCEDIR)/newpage.md \
	$(LOCAL_SOURCEDIR)/preface.md \
	$(LOCAL_SOURCEDIR)/newpage.md \
	$(LOCAL_SOURCEDIR)/update.md \
	$(LOCAL_SOURCEDIR)/newpage.md \
	$(LOCAL_SOURCEDIR)/cleardoublepage.md \
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
	$(SOURCEDIR)/2.01DivitionTypes.md \
	$(SOURCEDIR)/2.02Qualifications.md \
	$(SOURCEDIR)/2.03Exceptions.md \
	$(SOURCEDIR)/2.04ReclassificationOfProfessionalAmateur.md \
	$(SOURCEDIR)/2.05ProsPlayingAmAmsPlayingPro.md \
	$(SOURCEDIR)/2.06TrueAmateur.md \
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

$(TARGET): $(SOURCE) $(TEMPLATEDIR)/* $(CONFIGDIR)/* $(FILTERSDIR)/*
	$(PANDOC) \
		-d $(CONFIGDIR)/book.yaml \
		-d $(CONFIGDIR)/filters.yaml \
		-o $(TARGET) \
		$(SOURCE)

all: clean $(TARGET)

clean:
	rm -f $(TARGET)
