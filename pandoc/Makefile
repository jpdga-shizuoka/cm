PANDOC = pandoc
ENGINE = lualatex

NAME   = ディスクゴルフ大会のための競技マニュアル
TARGET = $(NAME).pdf
SOURCEDIR = ../source
SOURCEFILES = index.md \
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

$(TARGET): $(SOURCE)
	cat $(SOURCE) | \
	sed 's/\+\+//g' | \
	sed 's/<sup>\([0-9]\+\)<\/sup>/\\textsuperscript{\1}/g' | \
	$(PANDOC) \
		-C --pdf-engine=$(ENGINE) \
		--from markdown+superscript \
		--toc --toc-depth=2 \
		-V documentclass=ltjsarticle \
		-V luatexjapresetoptions=fonts-noto-cjk \
		-o $(TARGET)

all: clean $(TARGET)

clean:
	rm -f $(TARGET)
