PANDOC = pandoc
ENGINE = lualatex

NAME   = ディスクゴルフ大会のための競技マニュアル
TARGET = $(NAME).pdf
SOURCEDIR = ../source
SOURCE = $(SOURCEDIR)/index.md \
	$(SOURCEDIR)/Introduction.md \
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
	$(SOURCEDIR)/2.01Qualifications.md \
	$(SOURCEDIR)/2.02Exceptions.md \
	$(SOURCEDIR)/2.03ReclassificationOfProfessionalAmateur.md \
	$(SOURCEDIR)/2.04ProsPlayingAmAmsPlayingPro.md \
	$(SOURCEDIR)/2.05TrueAmateur.md \
	$(SOURCEDIR)/3.01General.md \
	$(SOURCEDIR)/3.02PaceOfPlay.md \
	$(SOURCEDIR)/3.03PlayerMisconduct.md \
	$(SOURCEDIR)/3.04DressCode.md \
	$(SOURCEDIR)/3.05CartsCaddiesAndGroups.md \
	$(SOURCEDIR)/3.06TourPlayerMediaAndSponsorRelations.md \
	$(SOURCEDIR)/3.07TourVendorPolicies.md \
	$(SOURCEDIR)/3.08TournamentDirectorRightsAndResponsibilities.md \
	$(SOURCEDIR)/4.01Applicability.md \
	$(SOURCEDIR)/4.02Eligibility.md \
	$(SOURCEDIR)/4.03CaddiesAndGroups.md \
	$(SOURCEDIR)/4.04PlayerCodeOfConduct.md \
	$(SOURCEDIR)/4.05RegistrationCheckingInAndBeginningPlay.md \
	$(SOURCEDIR)/4.06Scoring.md \
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
	$(SOURCEDIR)/6.01ApplicabilityExceptions.md \
	$(SOURCEDIR)/6.02VariancesORDG.md \
	$(SOURCEDIR)/6.03VariancesCM.md

$(TARGET): $(SOURCE)
	$(PANDOC) \
		-C --pdf-engine=$(ENGINE) \
		--from markdown+superscript \
		--toc --toc-depth=2 \
		-V documentclass=ltjsarticle \
		-V luatexjapresetoptions=fonts-noto-cjk \
		-o $(TARGET) \
		$(SOURCE)

all: clean $(TARGET)

clean:
	rm -f $(TARGET)
