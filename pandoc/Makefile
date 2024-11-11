NAME   = ディスクゴルフ大会のための競技マニュアル
TARGET = $(NAME)

PANDOC = pandoc

CONFIGDIR = config
TEMPLATEDIR = templates
FILTERSDIR = filters
SOURCEDIR = ../source
MARKDOWNDIR = markdown

CONFIG = $(CONFIGDIR)/body.yaml
COVERDATA = cover.tex
TEMPLATE = $(TEMPLATEDIR)/main.tex
SOURCEFILES = \
	Introduction.md \
	1.01PlayerEligibility.md \
	1.02TournamentRegistration.md \
	1.03WithdrawalsAndRefunds.md \
	1.04EventCheckIn.md \
	1.05PracticeRoundsBeginningPlayLateArrivals.md \
	1.06GroupingAndSectioning.md \
	1.07SuspensionOfPlay.md \
	1.08ReductionOfFieldSize.md \
	1.09Ties.md \
	1.10DistributionOfPrizes.md \
	1.11Officials.md \
	1.12TournamentOfficials.md \
	1.13YouthSafety.md \
	1.14Leagues.md \
	2.01Qualifications.md \
	2.02Exceptions.md \
	2.03ReclassificationOfProfessionalAmateur.md \
	2.04ProsPlayingAmAmsPlayingPro.md \
	2.05TrueAmateur.md \
	3.01General.md \
	3.02PaceOfPlay.md \
	3.03PlayerMisconduct.md \
	3.04DressCode.md \
	3.05CartsCaddiesAndGroups.md \
	3.06TourPlayerMediaAndSponsorRelations.md \
	3.07TourVendorPolicies.md \
	3.08TournamentDirectorRightsAndResponsibilities.md \
	4.01Applicability.md \
	4.02Eligibility.md \
	4.03CaddiesAndGroups.md \
	4.04PlayerCodeOfConduct.md \
	4.05RegistrationCheckingInAndBeginningPlay.md \
	4.06Scoring.md \
	5.01Applicability.md \
	5.02DivisionsReclassification.md \
	5.03PreparingCourse.md \
	5.04FinancesPayout.md \
	5.05TierTargetRequirements.md \
	5.06DidNotPlay.md \
	5.07ReportingRequirements.md \
	5.08MajorEliteSeriesRequirements.md \
	5.09A-TierRequirements.md \
	5.10X-DesignatedEvents.md \
	6.01ApplicabilityExceptions.md \
	6.02VariancesORDG.md \
	6.03VariancesCM.md
#
# ファイルとファイルが改行無しでくっ付いてしまう副作用に対処
#
define addnewline
	$(SOURCEDIR)/$(1) newlineonly.txt
endef
SOURCE = $(foreach file,$(SOURCEFILES),$(call addnewline,$(file)))

$(TARGET).pdf: $(SOURCE) $(COVERDATA)
	cat $(SOURCE) | \
	$(FILTERSDIR)/remove-plusplus | \
	$(FILTERSDIR)/link2dgjapan | \
	$(FILTERSDIR)/link2ordg | \
	$(FILTERSDIR)/table-markup | \
	$(FILTERSDIR)/footnote | \
	tee .md2pdf.md | \
	$(PANDOC) \
		-d $(CONFIGDIR)/common.yaml \
		-d $(CONFIGDIR)/body.yaml \
		-B $(COVERDATA) \
		-o $(TARGET).pdf

$(COVERDATA) : $(MARKDOWNDIR)/cover.md
	$(PANDOC) $(MARKDOWNDIR)/cover.md \
		-d $(CONFIGDIR)/common.yaml \
		-d $(CONFIGDIR)/cover.yaml \
		-o $(COVERDATA)

all: clean $(TARGET).pdf

clean:
	rm -f $(TARGET).html  $(TARGET).pdf $(COVERDATA) .md2pdf.md
